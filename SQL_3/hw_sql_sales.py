from flask import Flask, jsonify, request, Response
from SQL_3.database_handler import execute_query
from http import HTTPStatus

app = Flask(__name__)


@app.route('/sales')
def order_price():
    country = request.args.get('country', None)

    if country:
        query = """
        SELECT
            invoices.BillingCountry AS Country,
            SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS TotalSales
        FROM
            invoices
        JOIN
            invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        WHERE
            invoices.BillingCountry = ?
        GROUP BY
            invoices.BillingCountry
        """
        data = execute_query(query, (country,))
        if not data:
            return Response(f"No sales data found for country: {country}", status=HTTPStatus.NOT_FOUND)
    else:
        query = """
        SELECT
            invoices.BillingCountry AS Country,
            SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS TotalSales
        FROM
            invoices
        JOIN
            invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        GROUP BY
            invoices.BillingCountry
        """
        data = execute_query(query)
        if not data:
            return Response("No sales data found", status=HTTPStatus.NOT_FOUND)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
