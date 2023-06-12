from flask import Flask, jsonify, request
from flask import Response


app = Flask(__name__)


def check_credentials(username, password):
    print(username, password)
    return True


def auth_checker(auth):
    if not auth or not check_credentials(auth.username, auth.password):
        return 0

    return -1  # user Id for the future


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

