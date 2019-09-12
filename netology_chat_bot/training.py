import pandas as pd

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

phrases = ['привет', 'пока', 'как дела', 'расскажи анекдот', 'сделай рассылку студентам', 'какая погода', 'когда будет следующий урок?']
responses = ['привет, я чат-бот, твой друг', 'с нетерпением жду снова в гости', 'да все отлично, че сам как?', 'пока не умею рассказывать анекдоты', 'рассылка будет отправлена сразу, как научусь', 'посмотри лучше в интернете, я еще не умею ее предсказать', 'ты уже отучился, какие уроки']

tfidf=TfidfVectorizer(ngram_range=(1,3))
tfidf_vec=tfidf.fit_transform(phrases)



