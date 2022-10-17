import sqlite3

connection = sqlite3.connect('database.db')
database = connection.cursor()


def getAll():
    query = "SELECT * FROM product_types"
    cursor = database.execute(query)
    return cursor.fetchall()