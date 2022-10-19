import sqlite3
import datetime

connection = sqlite3.connect('database.db')
database = connection.cursor()

def getAll():
    query = "SELECT * FROM bills"
    cursor = database.execute(query)
    result = cursor.fetchall()
    connection.commit()
    return result


def add(data):
    try:
        query = "INSERT INTO bills(amount,date,customers_id) \
        VALUES('%s','%s','%s')" % (data['bill'][1] ,datetime.datetime.now() \
                ,data['bill'][0])
        cursor = database.execute(query)
        bill_id = cursor.lastrowid

        for i in data["products"]:
            query = "INSERT INTO products_bills(products_id,bills_id,quantity,price) \
                VALUES('%s','%s','%s','%s')" % (i[0],bill_id,i[1],i[2])
            database.execute(query)
            
        connection.commit() 
        return (1,)
    except Exception as e:
        print(e)
        return (-1,)

