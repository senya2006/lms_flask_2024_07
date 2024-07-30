from flask import Flask
import random
import string
import csv
import urllib.parse

app = Flask(__name__)


def generate_random_password():
    # Generate a random password with the special requirements

    length = random.randint(10, 20)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


generated_password = generate_random_password()


@app.route("/generate_password")
def generate_password():
    global generated_password
    generated_password = generate_random_password()
    encoded_password = urllib.parse.quote(generated_password)   # # URL Password Encoding
    return f"Generated Password: {generated_password}. Use this password in the URL as /calculate_average/{encoded_password}"


@app.route("/calculate_average/<password>")
def calculate_average(password):
    global generated_password
    decoded_password = urllib.parse.unquote(password)   # Decoding password from URL
    if decoded_password != generated_password:
        return "Invalid password!"

    # Calculate average height and weight from CSV
    with open('Flask_1/students.csv', mode='r') as file:
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