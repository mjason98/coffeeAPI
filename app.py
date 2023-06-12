from flask import Flask, jsonify, request
from flask import Response
from dotenv import load_dotenv
from services.auth import auth_checker

load_dotenv()

app = Flask(__name__)


@app.route('/v1/coffee/favourite', methods=['GET'])
def get_favorite_coffe():
    if auth_checker(request.authorization) == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    result = {'data': {
        "favouriteCofee": "espresso"
        }
              }
    return jsonify(result)


@app.route('/v1/admin/coffee/favourite/leadeboard', methods=['GET'])
def get_favorite_drinks():
    if auth_checker(request.authorization) == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    result = {'data': {
        "top3": [
            "espresso",
            "capuccino",
            "latte"
            ]
        }
              }

    return jsonify(result)


@app.route('/v1/coffee/favourite', methods=['POST'])
def post_favorite_coffes():
    if auth_checker(request.authorization) == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    result = {'data': {
        "top3": [
            "espresso",
            "capuccino",
            "latte"]
        }
              }

    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

