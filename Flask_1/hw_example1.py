from flask import Flask, request, jsonify
import random
import string
import pandas as pd
import io

app = Flask(__name__)


@app.route("/generate_password")
def generate_password():
    # Generate a random password with the following requirements:
    # - Length between 10 to 20 characters
    # - Contains upper and lower case letters, digits, and special symbols

    length = random.randint(10, 20)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return jsonify({"password": password})


@app.route("/calculate_average")
def calculate_average():
    # Calculate the average height and weight of students from a CSV file.

    password = request.args.get('password')

    if not password:
        return "Password parameter is missing!", 400

    csv_file = io.StringIO('Flask_1/students.csv')
    df = pd.read_csv(csv_file)

    # Calculate averages
    average_height = df['height'].mean()
    average_weight = df['weight'].mean()

    return jsonify({"average_height": average_height, "average_weight": average_weight})


if __name__ == "__main__":
    app.run(debug=True)
