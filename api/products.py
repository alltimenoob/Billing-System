import sqlite3

connection = sqlite3.connect('database.db')



def getAll():
    database = connection.cursor()
    query = "SELECT * FROM products"
    cursor = database.execute(query)
    result = cursor.fetchall()
    connection.commit()
    return result


def add(data):
    database = connection.cursor()
    query = "INSERT INTO products(products_name,quantity,price,products_types_id) \
    VALUES('%s','%s','%s','%s')" % (data['products_name'] ,data['quantity'] \
            ,data['price'] , data['products_types_id'][0])
    cursor = database.execute(query)
    connection.commit()
    return cursor.lastrowid