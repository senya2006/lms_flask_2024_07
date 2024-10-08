from flask import Flask, jsonify, Response
from webargs import fields
from webargs.flaskparser import use_kwargs
from SQL_3.database_handler import execute_query
from http import HTTPStatus

app = Flask(__name__)


@app.route('/sales')
@use_kwargs({'country': fields.Str(load_default=None)}, location="query")
def order_price(country):
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


@app.route('/track_info')
@use_kwargs({'track_id': fields.Int(required=True)}, location="query")
def get_all_info_about_track(track_id):
    query = """
    SELECT 
        tracks.TrackId,
        tracks.Name AS TrackName,
        albums.Title AS AlbumTitle,
        artists.Name AS ArtistName,
        genres.Name AS Genre,
        tracks.Composer,
        tracks.Milliseconds,
        tracks.Bytes,
        tracks.UnitPrice,
        COUNT(invoice_items.InvoiceLineId) AS PurchaseCount,
        GROUP_CONCAT(DISTINCT playlists.Name) AS Playlists -- The names of playlists that contain the track combined in a string.
    -- Table merge
    FROM tracks
    LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
    LEFT JOIN artists ON albums.ArtistId = artists.ArtistId
    LEFT JOIN genres ON tracks.GenreId = genres.GenreId
    LEFT JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
    LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    WHERE tracks.TrackId = ?
    GROUP BY 
        tracks.TrackId,
        tracks.Name,
        albums.Title,
        artists.Name,
        genres.Name,
        tracks.Composer,
        tracks.Milliseconds,
        tracks.Bytes,
        tracks.UnitPrice
    """
    data = execute_query(query, (track_id,))

    if not data:
        return Response(f"No data found for track ID: {track_id}", status=HTTPStatus.NOT_FOUND)

    # Dictionary with keys that describe each field
    result = {
        "TrackId": data[0][0],
        "TrackName": data[0][1],
        "AlbumTitle": data[0][2],
        "ArtistName": data[0][3],
        "Genre": data[0][4],
        "Composer": data[0][5],
        "Milliseconds": data[0][6],
        "Bytes": data[0][7],
        "UnitPrice": data[0][8],
        "PurchaseCount": data[0][9],
        "Playlists": data[0][10]
    }

    # Query to calculate the time of all tracks of all albums in hours
    query_total_time = """
    SELECT SUM(Milliseconds) / (1000.0 * 60 * 60) AS TotalHours
    FROM tracks
    """
    total_time_data = execute_query(query_total_time)

    # Query to calculate the time of all tracks of all albums in hours
    result["TotalTimeAllTracksInHours"] = total_time_data[0][0] if total_time_data else 0

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
