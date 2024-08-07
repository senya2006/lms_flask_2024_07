import sqlite3


def execute_query(query, args=()):
    db_path = 'C:/Users/shney/PycharmProjects/Hillel/lms_flask_2024_07/chinook.db'
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()

    return records
