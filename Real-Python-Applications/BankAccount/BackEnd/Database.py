import sqlite3




class Database:

    def __init__(self):
        self.create_banking_database()
        self.create_user_information_database()

    def create_user_information_database(self):
        self.connection = sqlite3.connect("Banking.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (account_number INTEGER PRIMARY KEY,first_name VARCHAR, last_name VARCHAR, adress VARCHAR,FOREIGN KEY(account_number)REFERENCES banking(account_id))")
        self.connection.commit()

    def create_banking_database(self):
        self.connection = sqlite3.connect("Banking.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS banking (account_id INTEGER PRIMARY KEY,amount FLOAT)")
        self.connection.commit()

    def insert(self,first_name,last_name,account_number,amount,address):
        self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",(account_number,first_name,last_name,address))
        self.connection.commit()
        self.cursor.execute("INSERT INTO banking VALUES (?,?)",(account_number,amount))
        self.connection.commit()

    def get_account_number(self):
        self.cursor.execute("SELECT account_number FROM users")
        rows = self.cursor.fetchall()
        return rows

    def search(self,account_number):
        self.cursor.execute("SELECT * FROM users WHERE account_number = ? ",(account_number))
        row = self.cursor.fetchall()
        return row

    def add_money(self,account_number,amount):
        self.cursor.execute("UPDATE banking SET amount = (? + ?) WHERE account_number= ?",(self.get_amount_account(account_number),amount,account_number))

    def withdraw_money(self,account_number,amount):
        self.cursor.execute("UPDATE banking SET amount = (? - ?) WHERE account_number= ?",
                            (self.get_amount_account(account_number), amount, account_number))

    def get_amount_account(self,account_number):
        self.cursor.execute("SELECT users.first_name,users.last_name,banking.amount from users,banking WHERE users.account_number = ? AND banking.account_id= ?",(account_number,account_number))
        amount_db = self.cursor.fetchall()
        return amount_db




