import csv
import httpx
from flask import Flask, request, Response
from faker import Faker
from http import HTTPStatus

app = Flask(__name__)
faker_inst = Faker()


@app.route("/generate-students")
def generate_students():
    count = int(request.args.get('count', 100))  # If the 'count' parameter is not passed, default value is 100
    count = min(count, 1000)  # Set a limit of 1000 students

    students = []
    for _ in range(count):
        first_name = faker_inst.first_name()
        last_name = faker_inst.last_name()
        email = faker_inst.email()
        password = faker_inst.password(length=10)
        birthday = faker_inst.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d')

        students.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'birthday': birthday
        })

    # Saving to a CSV file
    csv_filename = 'students.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'password', 'birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)

    return Response(f"Generated {count} students and saved to {csv_filename}", status=HTTPStatus.OK)


@app.route("/bitcoin_rate")
def get_bitcoin_value():
    currency = request.args.get('currency', 'USD').upper()
    convert = int(request.args.get('convert', 1))

    # Get the bitcoin rate for all currencies
    response = httpx.get("https://bitpay.com/api/rates")

    if response.status_code != HTTPStatus.OK:
        return Response("Unable to take bitcoin rates", status=response.status_code)

    rates = response.json()

    # Find the exchange rate for the selected currency
    rate = None
    for item in rates:
        if item['code'] == currency:
            rate = item['rate']
            break

    if rate is None:
        return Response("Currency not supported", status=HTTPStatus.BAD_REQUEST)

    # Calculate the cost in the selected currency
    total_value = rate * convert

    result_message = f"{total_value:,.2f} {currency} to buy {convert} BTC."
    return Response(result_message, status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(debug=True)
