from flask import Flask
import random
import string
import csv
import os

app = Flask(__name__)


@app.route("/generate_password")
def generate_password():
    while True:
        length = random.randint(10, 20)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        # Check if the password contains at least one digit, one uppercase letter, and one special character
        if (any(c.isdigit() for c in password) and
                any(c.isupper() for c in password) and
                any(c in string.punctuation for c in password)):
            break

    return f"Generated Password: {password}"


@app.route("/calculate_average")
def calculate_average():
    # Calculate average height and weight from CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(base_dir, 'students.csv')

    if not os.path.exists(csv_file_path):
        return f"CSV file not found! Expected at {csv_file_path}"

    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        heights = []
        weights = []
        for row in csv_reader:
            heights.append(float(row[1]))
            weights.append(float(row[2]))

        avg_height = sum(heights) / len(heights)
        avg_weight = sum(weights) / len(weights)

    return f"Average Height: {avg_height}, Average Weight: {avg_weight}"


if __name__ == "__main__":
    app.run(debug=True)
