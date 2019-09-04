from flask import Flask
from flask import request
from flask import make_response
# <<<<<<< HEAD
import os
# import json
# from requests import request
# =======
from flask import jsonify
# >>>>>>> d5dfe2b202277be95a2b3a8df23834c36f4d1cb5

app = Flask(__name__)

# создали ендпоинт
@app.route('/test', methods=['POST'])
def _test():
    # получили данные из запроса
    request_json = request.get_json()
    # тут ваш код возьмет запрос и вернет в ответ любой dict объект ответа, можно даже пустой
    # примерно так request_json -> response_body_json
    ...
#     response_body_json=request_json
#     response_body = json.dumps(response_body_json)
#     # упаковали все в корректный респонс
#     response = make_response(response_body)
#     response.headers['Content-Type'] = 'application/json'
#     # и вернули
# выведем функцию, которая будет возвращать 1, если вопрос есть в базе знаний и
#     response_body = request_json['test_val']
#     if response_body in ['test', 'hello']:
#         return 1
#     else:
#         return 0
    return '''<h1>
        {}
        </h1>'''.format(request_json['test_val'])





if __name__ == '__main__':
    # получили данные из запроса
    # request_json = request.get_json(silent=True, force=True)
    # # тут ваш код возьмет запрос и вернет в ответ любой dict объект ответа, можно даже пустой
    # # примерно так request_json -> response_body_json
    # ...
    # response_body_json = request_json
    # response_body = json.dumps(response_body_json)
    # # упаковали все в корректный респонс
    # response = make_response(response_body)
    # response.headers['Content-Type'] = 'application/json'
    # и вернули
    # port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=5000)
