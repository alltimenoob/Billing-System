import sqlite3
from types import NoneType

connection = sqlite3.connect('database.db')
database = connection.cursor()

def getOneByPhone(data):
    
    query = "SELECT * FROM customers WHERE customers_phone = '"+ data + "'"
    cursor = database.execute(query)
    result = cursor.fetchone()
    connection.commit()
    if result == None:
        return (-1,)
    return result
    
def getOneByEmail(data):
    query = "SELECT * FROM customers WHERE customers_email = '"+ data + "'"
    cursor = database.execute(query)
    result = cursor.fetchone()
    connection.commit()
    if result == None:
        return (-1,)
    return result

def getEmailById(data):
    query = "SELECT customers_email FROM customers WHERE customers_id = '"+ str(data) + "'"
    cursor = database.execute(query)
    result = cursor.fetchone()
    connection.commit()
    if result == None:
        return (-1,)
    return result

def add(data):
    try:
        query = "INSERT INTO customers(customers_name,customers_email,customers_phone) \
            VALUES('%s','%s','%s')" % (data[0] ,data[1] \
                    ,data[2])
        cursor = database.execute(query)
        connection.commit()
        return (cursor.lastrowid,data[0],data[1],data[2])
    except Exception as e:
        return (-1,)

    

