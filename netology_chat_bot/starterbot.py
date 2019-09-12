import os
import re
import time
# import slack
# from slackclient import SlackClient
# from slack import WebClient
from slackclient import SlackClient
# from sklearn.metrics.pairwise import cosine_similarity
# import scipy.spatial.distance.cosine

# from scipy import spatial
import numpy as np
import pandas as pd
import joblib


# instantiate Slack client
slack_client = SlackClient(os.environ.get('SlACK_TOKEN'))

# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
#
# phrases = ['привет', 'пока', 'как дела', 'расскажи анекдот', 'сделай рассылку студентам', 'какая погода', 'когда будет следующий урок?']
# responses = ['привет, я чат-бот, твой друг', 'с нетерпением жду снова в гости', 'да все отлично, че сам как?', 'пока не умею рассказывать анекдоты', 'рассылка будет отправлена сразу, как научусь', 'посмотри лучше в интернете, я еще не умею ее предсказать', 'ты уже отучился, какие уроки']

# df=pd.read_excel(r'C:\Users\vndan\projects\netology_chat_bot\kb\knowledge_base.xlsx', sheet_name='response')
df=pd.read_excel('knowledge_base.xlsx', sheet_name='response')

responses = df.реакция.tolist()
intent = df.интент.tolist()
target = df.класс.tolist()

# Загрузим классификаторы
# model = joblib.load(r'C:\Users\vndan\projects\netology_chat_bot\cls\basic_models.pk')
# tfidf_vec = joblib.load(r'C:\Users\vndan\projects\netology_chat_bot\cls\tfidf_vectoriser.pk')

model=joblib.load('basic_models.pk')
tfidf_vec = joblib.load('tfidf_vectoriser.pk')

prediction=model.predict_proba(tfidf_vec.transform(['узнать расписание занятий'])).tolist()[0]
pred_index=[i for i,j in enumerate(prediction) if j==max(prediction)]

if len(pred_index)>1:
    response = 'возможны 2 интента: ' + intent[pred_index[0]] + ' и ' + intent[pred_index[1]]
print(response)


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Не понимаю, попробуйте перефразировать вопрос"

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    # if command.startswith(EXAMPLE_COMMAND):
    #     response = "Sure...write some more code then I can do that!"

    # попробуем вывести овтеты из словаря, если текст сообщения будет более чем на 0,9 соответствовать сообщениям в словаре
    # scores = []
    # for sentence in phrases:
        # scores.append(cosine_similarity('првиет', sentence))
        # scores.append(1-scipy.spatial.distance.cosine(command, sentence))

    response = responses[int(np.argmax(model.predict(tfidf_vec.transpose(command))))-1]
    prediction = model.predict_proba(tfidf_vec.transform(['узнать расписание занятий'])).tolist()[0]
    pred_index = [i for i, j in enumerate(prediction) if j == max(prediction)]

    if len(pred_index) == 2:
        response = 'возможны 2 интента: ' + intent[pred_index[0]] + ' и ' + intent[pred_index[1]]
    else:
        response = responses[pred_index]


    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("чат-бот включился в работу")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("нет соединения с сервером!")