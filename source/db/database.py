import sqlite3

CLOSING = "Closing connetion to database."

#Create Database
connection = sqlite3.connect("restaurant.db")
# Create cursor
cursor = connection.cursor()

# Create table products
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    product_price REAL NOT NULL)""")

connection.commit()

# Create table Couriers

cursor.execute(""" CREATE TABLE IF NOT EXISTS couriers (
                    courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    courier_name TEXT NOT NULL,
                    courier_number TEXT NOT NULL)""")

connection.commit()

connection.close() 


# Products Table CRUD
def show_products_table() -> list:
    """This function shows all the items within the products table and returns the items as a list of tuples."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    # Query Database
    cursor.execute("SELECT * FROM products")
    
    items = cursor.fetchall()
    
    for item in items:
        print(f"""
              Product ID: {item[0]} | Product Name: {item[1]} | Product's Price: {item[2]} """)
    connection.close()
    return items

def insert_product(name: str, price: float):
    """This function allows the user to insert a new item (product name and product price)
    into the products table. """
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    # insert data
    try:
        cursor.execute("""INSERT INTO products (product_name, product_price) VALUES (?,?)""", (name, price))
        connection.commit()
        print("You've successfully entered in a new product.")
    except Exception as e:
        print(f"Error: {e}. An invalid input was detected. Please try again.")
    else:
        print(CLOSING)
    #close connection
    finally:
        connection.close()
    

def update_product(index: int, name: str, price: float):
    """This function allows user input to select with product item they would like to update 
    (product name and product price), then change the values with their preferred input."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    # update data
    
    cursor.execute("""SELECT product_id FROM products""")
    items = cursor.fetchall()
    
    result = [item[0] for item in items]
    
    try:
        
        if index not in result:
            print("This index is not valid in the table")
        else:
            cursor.execute("""UPDATE products SET product_name = (?), product_price = (?) 
                    WHERE product_id =(?)""", (name, price, index))
            connection.commit()
            print("You've successfully updated a product.")
    except Exception as e:
        print(f"Error: {e}. An invalid input was detected. Please try again.")
        
    else:
        print(CLOSING)
    finally:
    #close connection
        connection.close()

def delete_product(index: str):
    """This function allows to user to select which item from the products table they would like to delete."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    
    cursor.execute("""SELECT product_id FROM products""")
    items = cursor.fetchall()
    
    result = [item[0] for item in items]
    
    try:
        if int(index) not in result:
            print("This index is not valid in the table")
        else:
        # delete data
            cursor.execute("""DELETE FROM products WHERE product_id = (?)""", (index,))
            connection.commit()
            print("You've successfully deleted a product.")
    except Exception as e:
        print(f"Error: {e}. A non valid input was detected. Please try again.")
    else:
        print("\n")
        print(CLOSING)
        print("\n")
    finally:
    #close connection
        connection.close()

# Couriers Table CRUD
def show_couriers_table() -> list:
    """This function allows the user to view all the items within the couriers table. It returns a list 
    tuples containing all the items."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    # Query Database
    cursor.execute("SELECT * FROM couriers")
    
    items = cursor.fetchall()
    
    for item in items:
        print(f"""
              Courier ID: {item[0]} | Courier Name: {item[1]} | Courier's Number: {item[2]} """)
    connection.close()
    return items

def insert_courier(name: str, number: str):
    """This function allows the user to insert a new item into the couriers table 
    (courier name and courier phone number)."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    # insert data
    try:
        cursor.execute("""INSERT INTO couriers (courier_name, courier_number) VALUES (?,?)""", (name, number))
        connection.commit()
        print("You've successfully entered in a new courier.")
        print("\n")
    except Exception as e:
        print(f"Error: {e}. Invalid input detected. Please try again.")
    #close connection
    else:
        print(CLOSING)
    finally:
        connection.close()
    

def update_courier(index: int, name: str, number: str):
    """This function allows the user to select an item from the couriers table, and update the values
    of the couriers name and couriers phone number."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    
    #Confirm User select
    cursor.execute("""SELECT courier_id FROM couriers""")
    items = cursor.fetchall()
    
    result = [item[0] for item in items]
    
    try:
        if index not in result:
            print("This index is not valid in the table")
        else:
        
            # update data
            cursor.execute("""UPDATE couriers SET courier_name = (?), courier_number = (?) 
                    WHERE courier_id =(?)""", (name, number, index))
            connection.commit()
            print("You've successfully updated in a courier.")
            print("\n")
    except Exception as e:
        print(f"Error: {e}. An Invalid input was detected. Please try again.")
    else:
        print(CLOSING)
    finally:
    #close connection
        connection.close()

def delete_courier(index: str):
    """This function allow the user to select an item from the couriers table to delete."""
    #Connect to database
    connection = sqlite3.connect("restaurant.db")
    # Create a cursor
    cursor = connection.cursor()
    
    cursor.execute("""SELECT courier_id FROM couriers""")
    items = cursor.fetchall()
    
    result = [item[0] for item in items]
    
    try:
        if int(index) not in result:
            print("This index is not valid in the table")
        else:
        # delete data
            cursor.execute("""DELETE FROM couriers WHERE courier_id=(?)""", (index,))
            connection.commit()
            print("You've successfully deleted a courier.")
            print("\n")
    except Exception as e:
        print(f"Error: {e}. An invalid input was detected. Please try again.")
    else:
        print(CLOSING)
    finally:
    #close connection
        connection.close()
    

# To remember the names of the columns use this below ->:
# conn = sqlite3.connect('restaurant.db')
# cursor = conn.execute('select * from couriers')
# print(cursor.description)
# conn.close()
