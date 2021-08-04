
from db.database import show_couriers_table
from the_handlers.logos import main_menu_logo,couriers_menu_logo,products_menu_logo,orders_menu_logo
import csv
import os
import time 
#########################################################################
#TODO
# Create csv file for orders
# Place csv file in data folder
# UNIT TEST!!!!
# Push/commit everything to github

##########################################################################

    
def clear_screen_timer():
    """This function gives a timer of 3 seconds after the user ends the app before it clears the screen."""
    time.sleep(3)
    os.system("cls")

# Menu Options 
def main_menu():
    """ The purpose of this function is to give the user the option to access the products menu, couriers menu, or exit the application."""
    print(main_menu_logo)
    
    main_menu_options = """
    Welcome to the main menu, the options are:
    0) Exit App
    1) Proceed to Products Menu
    2) Proceed to Couriers' Menu
    3) Proceed to Orders' Menu
    """
    print(main_menu_options)
    
def products_menu():
    """The purpose of this function enables the user choose from the options to return to main menu, 
    view products list, add new products, delete products, and edit existing products."""
    
    print(products_menu_logo)
    
    product_menu_options = """
    Welcome to the products menu, your options are:
    0) Return to main menu
    1) Show current products list
    2) Add a new item to the products list
    3) Edit an existing item from the products list
    4) Delete an item from the products list
    """
    print(product_menu_options)


def couriers_menu():
    """The purpose of this function enables the user choose from the options to return to main menu, 
    view couriers' list, add new couriers, delete couriers, and edit existing couriers."""
    
    print(couriers_menu_logo)
    
    couriers_menu_options = """
    Welcome to the couriers menu, your options are:
    0) Return to main menu
    1) Show current couriers list
    2) Add a new person to the couriers list
    3) Edit an existing person from the couriers list
    4) Delete a person from the couriers list
    """
    print(couriers_menu_options)


def orders_menu():
    """
    The purpose of this function enables the user choose from the options to return to main menu, 
    view orders list, add an order to orders list, update an existing order, update an existing order status,
    and delete an existing order.
    """
    
    print(orders_menu_logo)
    
    order_menu_options = """
    Welcome to the Order Menu, the options are:
    0) Return to main menu
    1) Show current orders
    2) Place an order
    3) Update an existing order's status
    4) Update an existing order
    5) Delete an order
    """
    print(order_menu_options)
    
################################################################################################################
    # Products Menu functions
    
def get_product_name() -> str:
    """This function checks to make sure products name isn't an empty string. It returns a string."""

    try:
        product_name = input("What is the name of this product?: ").title()
        if product_name == "":
            raise ValueError()
    except ValueError:
        print(f"Error: No name was detected in the input.")
    else:
        return product_name
    
def validate_product_price() -> float:
    """"Checks to confirm user inputted a numeric number that can be converted into a decimal number.
    It returns a float"""
    try:
        product_price = float(input("Set price of product: £ "))
    except Exception as e:
        print(f"Error: {e} An invalid input was detected.")
    else:
        return product_price

def select_item_update() -> int:
    """This function takes in user input of the item they wish to update and returns a integer."""
    try:
        item_selection = int(input("What item would you like to update? Please enter the number of the ID: "))
    except Exception as e:
        print(f"Error: {e}. A non-integer was detected. Please try again.")
    else:
        return item_selection
    

def select_item_delete() -> str:
    """This function takes in user input of the item they wish to update and returns a string."""
    try:
        item_selection = input("What item would you like to delete? Please enter the number of the ID: ")
        if item_selection.isnumeric() == False:
            raise ValueError
    except ValueError:
        print(f"Error: a non-integer was detected. Please try again.")
    except Exception as e:
        print(f"Error: {e}. A non-integer was detected. Please try again.")
    else:
        return item_selection

################################################################################################################      
    # Courier Menu Functions
    
def get_courier_name() -> str:
    
    """This function checks user input for an empty string and checks if any digits were inputted into the 
    customer name. It returns a string."""
    try:
        courier_name = input("What is the name of the courier?: ").title()
        if courier_name == "" or courier_name.isnumeric() == True:
            raise ValueError
    except ValueError:
        print(f"Error: An invalid character was detected in in your entry. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        return courier_name
    
    
def validate_phone_number() -> str:
    """Checks to confirm user input is an 11 digit number, and not an empty string. This
    function returns a string."""
    try:
        courier_phone = input("Please enter a valid U.K. phone number: +44 ")
        if courier_phone == "" or courier_phone.isdigit() == False or len(courier_phone) != 11:
            raise ValueError
    except ValueError:
        print(f"Error: An invalid phone number was entered. Please try again.")
    else:
        return courier_phone
    
################################################################################################################    
    # Orders Menu Functions
    
    
def show_current_list(List: list):
    """This function takes in a list and 
    gives the user an enumerates print out of all the items within the list."""
    
    for index, item in enumerate(List):
        print(f"ID: {index}, Value: {item}")
    return List    

def get_customer_name() -> str:
    """This function checks user input for an empty string and if any digits were inputted. This function
    returns a string."""
    try:
        customer_name = input("Please enter your name: ").title()
        if customer_name == "":
            raise ValueError
    except ValueError:
        print(f"Error: An invalid character was detected in the name. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        return customer_name

def get_customer_address() -> str:
    """This function receives user input for customer address and returns a string."""
    customer_address = input("Please enter your address: ").upper()
    return customer_address

# Use Validate phone number function to get customer number

def get_customer_orders() -> list:
    """This function takes user input for amount of orders they would like to place, and makes a list from it.
    this function returns a list."""
    customer_orders = input("Please enter the items you'd like to order all separated by commas: ").split(",")
    
    try:
        basket = [int(item) for item in customer_orders]
    except Exception as e:
        print(f"Error: a non-integer was detected. Please try again.")
    else:
        return basket
    
def get_customer_courier():
    """This function takes in user input about which courier they'd like to select"""

    rows = show_couriers_table()
    couriers_table = [row[0] for row in rows]
    
    try:
        customer_courier = int(input("Please input the ID of the courier you'd like: "))
        if customer_courier not in couriers_table:
            raise IndexError
    except IndexError:
        print("Error: The courier ID you've selected doesn't exist. Please try again.")
    except Exception as e:
        print(f"Error: {e}.")
    else:
        return customer_courier

# Make a function to create a new order
def make_new_order(current_orders: list, customer_name: str, customer_number: str, customer_address: str, courier_identification: int, basket_items: list, status="Preparing"):
    current_orders.append({"Customers' Name": customer_name, "Customers' Address": customer_address,\
                    "Customers' Phone Number": customer_number, "Courier": courier_identification,\
                        "Status": status, "Items": basket_items})
    print("\n")
    print("Your order has been placed.")
                
    return current_orders


def update_order(List: list, selected_list):
    try:
        if int(selected_list) > len(List) - 1 or  int(selected_list) < 0: #Checks user inputs index range 
            raise IndexError
        else:
            updated_list = List[int(selected_list)]
                        
    except IndexError:
        print("Error: Index error. Please try again.")
    except Exception as e:
        print(f"Error: {e}, Please try again.")
                    
    else:
        # Bug: Can change values in list to anything
        for key, value in updated_list.items():
            print(f"Current Key: {key}, Current Value: {value}")
            print("\n")
            value_change = input("What would you like the new this new value to be?: ").title()
            if value_change == "":
                print("\n")
                print("You haven't inputted anything to change the value")
            else:
                List[int(selected_list)][key] = value_change
    return List

def update_order_status(orders:list, orders_status: list, orders_status_index: str, order_index_value: str):
    try:
        if int(orders_status_index) > len(orders_status) - 1 or int(orders_status_index) < 0:
            print("Your order's status is out of range.")
            raise IndexError
            
        elif int(order_index_value) > len(orders) - 1 or int(order_index_value) < 0:
            print("Your orders' index value is out of range.")
            raise IndexError
            
        else:
            orders[int(order_index_value)]["Status"] = orders_status[int(orders_status_index)]
    except IndexError:
        print("Error: Index is out of range.")
    except Exception as e:
        print(f"Error: {e}. Please try again.")   

    else:
        print("Your orders' status has been updated. Here is your new order:")
        print(orders[int(order_index_value)])
        return orders   


def delete_order(List: list, remove_item: str) -> list:
    """This function takes in a list and user input to delete an item from the list. It returns the new list."""
    try:
        if int(remove_item) < 0 or int(remove_item) > len(List) - 1:
            raise IndexError
        else:
            del List[int(remove_item)]
                    
    except IndexError:
        print("Error: Index value error")
    except Exception as e:
        print(f"Error: {e}, please try again.")
                
    else:
        print("You've successfully removed the item.")
        print("\n")
        return List

#############################################################################################################
# Save file to Csv

def save_to_csv_dict(file_path: str, file_keys: list):
    #keys = file_keys[0].keys()
    with open(file_path, "w", newline= "") as output_file:
        keys = file_keys[0].keys()
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(file_keys)
        
def read_from_csv_dict(file_path: str):
    with open(file_path,"r") as input_file:
        reader = csv.DictReader(input_file)
        variable= [item for item in reader]
        return variable
