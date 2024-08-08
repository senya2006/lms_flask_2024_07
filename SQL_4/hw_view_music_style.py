from flask import Flask, jsonify, Response
from webargs import fields
from webargs.flaskparser import use_kwargs
from http import HTTPStatus
from SQL_3.database_handler import execute_query

app = Flask(__name__)


@app.route('/stats_by_city')
@use_kwargs({"genre": fields.Str(required=True)}, location="query")
def stats_by_city(genre):
    # SQL query to get GenreId by genre name
    genre_query = "SELECT GenreId FROM genres WHERE Name = ?"
    genre_result = execute_query(genre_query, (genre,))

    if not genre_result:
        return Response(f"Genre '{genre}' not found", status=HTTPStatus.NOT_FOUND)

    genre_id = genre_result[0][0]

    # SQL query to retrieve the cities with the highest number of listens for a specified genre
    city_query = """
    SELECT customers.City, COUNT(invoice_items.InvoiceLineId) as ListenCount
    FROM customers
    JOIN invoices ON customers.CustomerId = invoices.CustomerId
    JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    JOIN tracks ON invoice_items.TrackId = tracks.TrackId
    WHERE tracks.GenreId = ?
    GROUP BY customers.City
    HAVING ListenCount = (
        SELECT MAX(ListenCount)
        FROM (
            SELECT COUNT(invoice_items.InvoiceLineId) as ListenCount
            FROM customers
            JOIN invoices ON customers.CustomerId = invoices.CustomerId
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            JOIN tracks ON invoice_items.TrackId = tracks.TrackId
            WHERE tracks.GenreId = ?
            GROUP BY customers.City
        )
    )
    ORDER BY ListenCount DESC
    """
    city_result = execute_query(city_query, (genre_id, genre_id))

    if not city_result:
        return Response(f"No data found for genre '{genre}'", status=HTTPStatus.NOT_FOUND)

    cities = [{"city": row[0], "count": row[1]} for row in city_result]
    return jsonify({"genre": genre, "cities": cities})


if __name__ == '__main__':
    app.run(debug=True)
