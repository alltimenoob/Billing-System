import sqlite3
from types import NoneType

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
        if "" in data:
            if data[2] != "":
                query = "SELECT * FROM customers WHERE customers_phone = "+str(data[2])
            if data[1] != "":
                query = "SELECT * FROM customers WHERE customers_email = '"+str(data[1]+"'")
            cursor = database.execute(query)
            row = cursor.fetchone()
            if row != None :
                return row
        if "" not in data:
            query = "INSERT INTO customers(customers_name,customers_email,customers_phone) \
            VALUES('%s','%s','%s')" % (data[0] ,data[1] \
                    ,data[2])
            cursor = database.execute(query)
            connection.commit()
            return (cursor.lastrowid,data[0],data[1],data[2])
    except Exception as e:
        print(e)
        return (-1,)
    return (0,)

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
