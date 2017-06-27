import sqlite3


def create_table():
    # Connect to database
    connection = sqlite3.connect("lite.db")
    # Set cursor
    cursor = connection.cursor()
    # Create Database Table if it does not exist
    cursor.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER , price REAL )")
    # Commit changes
    connection.commit()
    # Close connection
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))
    connection.commit()
    connection.close()


def update(quantity, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity = ? WHERE item = ?", (quantity, item))
    connection.commit()
    connection.close()


create_table()
# insert('Coffe Cup', 10, 4)
# insert("Beer Glass", 50, 10.9)
print(view())
# delete("Beer Glass")
update(100, "Beer Glass")
print(view())
