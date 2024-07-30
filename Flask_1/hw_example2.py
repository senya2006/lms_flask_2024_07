from flask import Flask, request
import random
import string
import csv

app = Flask(__name__)


@app.route("/generate_password")
def generate_password():

    # Generates a random password with a length from 10 to 20 characters,
    # including upper and lower case letters, digits, and special symbols.

    length = random.randint(10, 20)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return f"Generated Password: {password}. Use this password in the URL as /calculate_average/{password}"


@app.route("/calculate_average/<password>")
def calculate_average(password):

    # Verifies the password and calculates the average height and weight of students from a CSV file.

    if password != "correct_password":
        return "Invalid password!"

    total_height = 0
    total_weight = 0
    count = 0

    with open('Flask_1/students.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_height += float(row['Height'])
            total_weight += float(row['Weight'])
            count += 1

    average_height = total_height / count
    average_weight = total_weight / count

    return f"Average Height: {average_height:.2f} cm, Average Weight: {average_weight:.2f} kg"


if __name__ == "__main__":
    app.run(debug=True)
