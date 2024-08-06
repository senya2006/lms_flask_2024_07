from flask import Flask
from SQL_3.database_handler import execute_query

app = Flask(__name__)


@app.route('/customers')
def get_all_customers():
    query = "SELECT * FROM customers"
    data = execute_query(query=query)
    return data


if __name__ == "__main__":
    app.run(debug=True)
