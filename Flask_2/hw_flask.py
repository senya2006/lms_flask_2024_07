import csv
import httpx
from flask import Flask, request, Response
from faker import Faker
from http import HTTPStatus
from webargs.flaskparser import use_kwargs
from Flask_2.student_count_config import student_count_config
from Flask_2.bitcoin_rate_config import bitcoin_rate_config

app = Flask(__name__)
faker_inst = Faker()


@app.route("/generate_students")
@use_kwargs(student_count_config, location="query")
def generate_students(count):
    # Set a limit of 1000 students
    count = min(count, 1000)

    students = []
    csv_filename = 'students.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'password', 'birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(count):
            student = {
                'first_name': faker_inst.first_name(),
                'last_name': faker_inst.last_name(),
                'email': faker_inst.email(),
                'password': faker_inst.password(length=10),
                'birthday': faker_inst.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d')
            }
            students.append(student)
            writer.writerow(student)

    response_data = "\n".join(
        f"{student['first_name']} {student['last_name']}, Email: {student['email']}, Password: {student['password']}, "
        f"Birthday: {student['birthday']}"
        for student in students
    )

    return Response(response_data, status=HTTPStatus.OK)


@app.route("/bitcoin_rate")
@use_kwargs(bitcoin_rate_config, location="query")
def get_bitcoin_value(currency, convert):
    # Get the bitcoin rate for all currencies
    response = httpx.get("https://bitpay.com/api/rates")

    if response.status_code != HTTPStatus.OK:
        return Response("Unable to fetch bitcoin rates", status=response.status_code)

    rates = response.json()

    # Find the exchange rate for the selected currency
    rate = None
    for item in rates:
        if item['code'] == currency.upper():
            rate = item['rate']
            break

    if rate is None:
        return Response("Currency not supported", status=HTTPStatus.BAD_REQUEST)

    # Calculate the cost in the selected currency
    total_value = rate * convert

    # Move result message to the response
    return Response(f"{total_value:,.2f} {currency} to buy {convert} BTC.", status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(debug=True)
