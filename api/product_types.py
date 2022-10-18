import sqlite3

connection = sqlite3.connect('database.db')
database = connection.cursor()


def getAll():
    query = "SELECT * FROM product_types"
    cursor = database.execute(query)
    return cursor.fetchall()

def add(data):
    try:
        query = "INSERT INTO product_types(product_types_name) VALUES('%s')"%(data)
        database.execute(query)
        connection.commit()
    except:
        return -1
    return 1

def update(data):
    try:
        query = "UPDATE product_types set product_types_name = '%s' WHERE product_types_id = '%s'"%(data[1],data[0])
        database.execute(query)
        connection.commit()
    except Exception as e:
        print(e)
        return -1
    return 1