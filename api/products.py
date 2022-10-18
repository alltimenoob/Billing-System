import sqlite3

connection = sqlite3.connect('database.db')
database = connection.cursor()

def getAll():
    query = "SELECT * FROM products"
    cursor = database.execute(query)
    result = cursor.fetchall()
    connection.commit()
    return result


def add(data):
    try:
        query = "INSERT INTO products(products_name,quantity,price,products_types_id) \
        VALUES('%s',%s,%s,%s)" % (data['products_name'] ,data['quantity'] \
                ,data['price'] , data['products_types_id'])
        print(query)

        cursor = database.execute(query)
        connection.commit()
    except Exception as e:
        print(e)
        return -1
    return cursor.lastrowid

def update(data):
    print(data)
    try:
        query = "UPDATE products set products_name = '%s', quantity = '%s', price ='%s' \
        , products_types_id = '%s' WHERE products_id = '%s'" % ( data['products_name'] ,\
         data['quantity']  ,data['price'] , data['products_types_id'],data['product_id'])
        database.execute(query)
        connection.commit()
    except:
        return -1

    return 1
