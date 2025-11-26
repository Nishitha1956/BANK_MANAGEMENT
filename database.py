import mysql.connector as sql

mydb = sql.connect(
    host="127.0.0.1",
    user="root",
    password="Nishuv#41",
    database="bank"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result
# For INSERT, UPDATE, DELETE
def db_insert(query):
    cursor.execute(query)
    mydb.commit()
    return True


def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_no INTEGER NOT NULL,
                status BOOLEAN NOT NULL)
    ''')

mydb.commit()
if __name__ == "__main__":
    createcustomertable()
