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
    return '''<h1>
        {}
        </h1>'''.format(request_json['test_val'])





if __name__ == '__main__':
    app.run(debug=False, port=5000)
