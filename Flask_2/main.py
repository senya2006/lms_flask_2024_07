import pprint
import random
import string
from http import HTTPStatus

import httpx
from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate

app = Flask(__name__)


@app.route("/admin")
def hello_world():
    # view
    return "<p>Hello, World!!!!</p>"


@app.route("/generate-password")
@use_kwargs(
    {
        "length": fields.Int(
            missing=10,
            validate=[validate.Range(min=8, max=100, min_inclusive=True, max_inclusive=True)],
        )
    },
    location="query"
)
def generate_password(length):
    # password_length = request.args.get("length", '10')
    # max_limit = request.args.get("max_limit", '100')
    #
    # if not password_length.isdigit():
    #     return "Error: length should be a number!"
    #
    # password_length = int(password_length)
    #
    # if not 8 <= password_length <= 100:
    #     return "Error: length should be between 8 and 100!"

    return "".join(
        random.choices(
            string.digits + string.ascii_letters + string.punctuation, k=length
        )
    )


@app.route("/get-astronauts")
def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    result = httpx.get(url=url, params={})

    if result.status_code not in (HTTPStatus.OK,):
        return Response("Error: Something went wrong with the api.open-notify.org!",
                        status=result.status_code)

    result: dict = result.json()
    statistics = {}
    for entry in result.get('people', {}):
        statistics[entry['craft']] = statistics.get(entry['craft'], 0) + 1

    pprint.pprint(result)
    return statistics

# kiss - keep it simple, stupid!

# status code
# 100 - informational
# 200 - OK
# 300 - Redirect
# 400 - client error
# 500 - server error

# Camel_case - classes
# snake_case - all python code except classes
# kebab-case - for urls


app.run(port=5001,
        # debug=True
        )

# http://127.0.0.1:5001/profile?a=1
# http://127.0.0.1:5001/about/

# POST тіло запиту, захищена
# використовується для змін в сервері
# GET все буде знаходитись в url і не можна використовувати важливу інформацію, не захищенна
# використовується для фільтрування, має параметри, після "?" пишемо параметри, & - амперсант для розділення параметрів
