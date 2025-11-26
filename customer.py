
from database import *
class Customer:
    def __init__(self, username, password, name, age, city, account_no, balance=0, status=True):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.account_no = account_no
        self.balance = balance
        self.status = status
    def createuser(self):
        query = f"""
        INSERT INTO customers (username, password, name, age, city, account_no, balance, status)
        VALUES ('{self.username}', '{self.password}', '{self.name}', {self.age}, '{self.city}', 
        '{self.account_no}', {self.balance}, {self.status});
        """
        db_insert(query)
        print("🎉 User Created & Saved in Database Successfully!")