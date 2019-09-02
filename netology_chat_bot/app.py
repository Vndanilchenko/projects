from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

app = Flask(__name__)

# создали ендпоинт
@app.route('/webhook')
def hello_slack():
    # получили данные из запроса
    request_json = flask.request.get_json(silent=True, force=True)
    # тут ваш код возьмет запрос и вернет в ответ любой dict объект ответа, можно даже пустой
    # примерно так request_json -> response_body_json
    ...
#     response_body = json.dumps(response_body_json)
#     # упаковали все в корректный респонс
#     response = make_response(response_body)
#     response.headers['Content-Type'] = 'application/json'
#     # и вернули
#     return response
# выведем функцию, которая будет возвращать 1, если вопрос есть в базе знаний и 
    response_body = json.dumps(request_json)
    if response_body in ['test hello']
        return jsonify(1)
    else:
        return jsonify(0)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
