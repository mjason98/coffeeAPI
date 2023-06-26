from flask import Flask, jsonify, request
from flask import Response
from flask import make_response
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


from services.auth import auth_checker
from services.coffee import get_best_coffee
from services.coffee import get_top3_coffee
from services.coffee import set_top3_coffee
from services.init_data import init_data
from services.auth import auth_limiter_function


load_dotenv()
init_data()


app = Flask(__name__)
limiterusr = Limiter(
        key_func=auth_limiter_function,
        app=app)

limiteradr = Limiter(
        key_func=get_remote_address,
        app=app)


@app.route('/v1/coffee/favourite', methods=['GET'])
@limiteradr.limit("10/minute")
def get_favorite_coffe():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    best_coffee = get_best_coffee(userid)

    result = {'data': {
        "favouriteCofee": best_coffee
        }
              }
    return jsonify(result)


@app.route('/v1/admin/coffee/favourite/leadeboard', methods=['GET'])
@limiterusr.limit("3/minute")
def get_favorite_drinks():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    top3 = get_top3_coffee(userid)

    result = {'data': {"top3": list(top3)}}

    return jsonify(result)


@app.route('/v1/coffee/favourite', methods=['POST'])
@limiteradr.limit("10/minute")
def post_favorite_coffes():
    userid = auth_checker(request.authorization)
    if userid == 0:
        return Response('Unauthorized', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    body = request.get_json()['top3']

    set_top3_coffee(userid, body)

    top3 = get_top3_coffee(userid)

    result = {'data': {"top3": list(top3)}}

    return jsonify(result)


@app.route('/v1/healthcheck', methods=['GET'])
def healh_check():
    response = make_response("OK")
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
