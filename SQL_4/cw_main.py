from flask import Flask
from webargs import fields
from webargs.aiohttpparser import use_kwargs

from SQL_3.database_handler import execute_query

app = Flask(__name__)


@app.route('/customers')
@use_kwargs(
    {
        "first_name": fields.Str(
            required=True,
        ),
        "last_name": fields.Str(
            load_default=None
        )
    },
    location="query"

)
def get_all_customers(first_name, last_name):
    query = "SELECT FirstName, LastName FROM customers"

    fields = {}

    if first_name:
        fields["first_name"] = first_name
    if last_name:
        fields["last_name"] = last_name

    if fields:
        query += " WHERE " + " AND ".join(
            f"{key}=?" for key in fields
        )

    data = execute_query(query=query, args=tuple(fields.values))

    return '<br>'.join(str(record) for record in data)


if __name__ == "__main__":
    app.run(debug=True)

# blueprints - в контексті Flask, це як підпроекти в самому проекті

# sql injection
# /customers?last_name=Miller&first_name='Dan' OR 1=1 --
# back door дістаємо інфу яку не можемо просто получити з бази данних
# SELECT FirstName, LastName FROM customers WHERE FirstName='Dan' OR 1=1 --'AND LastName='Miller'

# /customers?last_name=Miller&first_name='Dan' union all select Total, BillingAddress from invoices --
# SELECT FirstName, LastName FROM customers WHERE FirstName='Dan'
#                                            union all select Total, BillingAddress from invoices
#                                            -- 'AND LastName='Miller''

# Пошук по назвам стовбців
# SELECT name FROM main.sqlite_master WHERE type='table';
# SELECT name FROM PRAGMA_TABLE_INFO('invoices');

# щоб видалити таблицю
# /customers?last_name=Miller&first_name='Dan'; delete from new_customers; --

# SELECT Email FROM customers WHERE Email like '%!_%' ESCAPE '!'; -- видає емейли з "_" і ми вибрали "!"
