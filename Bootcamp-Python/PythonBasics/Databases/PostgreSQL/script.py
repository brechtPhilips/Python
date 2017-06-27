import psycopg2


def create_table():
    # Connect to database
    connection = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432' ")
    # Set cursor
    cursor = connection.cursor()
    # Create Database Table if it does not exist
    cursor.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER , price REAL )")
    # Commit changes
    connection.commit()
    # Close connection
    connection.close()


def insert(item, quantity, price):
    connection = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s ",(item,))
    connection.commit()
    connection.close()


def update(quantity, item):
    connection = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity = %s WHERE item = %s", (quantity, item))
    connection.commit()
    connection.close()


create_table()
insert("Orange", 10, 9)
# delete("Orange")
update(50, "Orange")
print(view())
