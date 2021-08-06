from the_handlers.module import save_to_csv_dict, read_from_csv_dict # CSV Functions
from the_handlers.module import clear_screen_timer
from db.database import show_products_table, delete_product, update_product, insert_product # Database (products)
from db.database import show_couriers_table, delete_courier, update_courier, insert_courier # Database (couriers)
from the_handlers.module import main_menu, products_menu, couriers_menu, orders_menu # Menu options
from the_handlers.module import get_product_name, validate_product_price # Products Functions
from the_handlers.module import select_item_delete, select_item_update # Products & Courier functions
from the_handlers.module import get_courier_name, validate_phone_number # Courier Functions
from the_handlers.module import show_current_list, get_customer_name, get_customer_address, get_customer_orders #Orders Functions
from the_handlers.module import make_new_order, update_order_status, delete_order, get_customer_courier, update_order #Orders Functions

orders = read_from_csv_dict("data/orders.csv")

orders_status = ["Order pending", "Preparing", "Out for Delivery", "Delievered"]

application_on = True

while application_on:


    main_menu()

    main_menu_choice = input("What would you like todo? Please enter a number listed above or type 'Exit' to quit: ").title()

    if main_menu_choice == "0" or main_menu_choice == "Exit":
        # Make csv file to save orders
        save_to_csv_dict("data/orders.csv", orders)
        application_on = False
        exit_app = input("Thank you for using our app! Enter any button to exit: ")
        clear_screen_timer()
        exit()
        

    elif main_menu_choice == "1":
        products_menu_on = True
        while products_menu_on:
            products_menu()
        
            products_menu_choice = input("Please enter a number listed above or type 'Exit' to quit: ").title()
        
            if products_menu_choice == "0" or products_menu_choice == "Exit":
                # return to main menu
                print("Returning to main menu.")
                products_menu_on = False
            
            elif products_menu_choice == "1":
                # Show current data
                show_products_table()
            
            elif products_menu_choice == "2":
                # insert item
                product_name = get_product_name()
                product_price = validate_product_price()
                insert_product(product_name, product_price)
                
            elif products_menu_choice == "3":
                # update item
                show_products_table()
                item_selection = select_item_update()
                product_name = get_product_name()
                product_price = validate_product_price()
                
                update_product(item_selection, product_name, product_price)
            elif products_menu_choice == "4":
                # delete item
                show_products_table()
                selection_item = select_item_delete()
                delete_product(selection_item)
            else:
                print("Invalid entry detected, returning back to products menu")
        
    elif main_menu_choice == "2":
        couriers_menu_on = True
        while couriers_menu_on:
            couriers_menu()
            
            couriers_menu_choice = input("Please enter a number listed above, or type 'Exit' to quit: ").title()
            
            if couriers_menu_choice == "0" or couriers_menu_choice == "Exit":
                # return to main menu
                print("Returning to main menu")
                couriers_menu_on = False
                
            elif couriers_menu_choice == "1":
                # Show current data
                show_couriers_table()
                
            elif couriers_menu_choice == "2":
                #insert item
                courier_name = get_courier_name()
                courier_number = validate_phone_number()
                insert_courier(courier_name, courier_number)            
            
            elif couriers_menu_choice == "3":
                # update item
                show_couriers_table()
                item_selection = select_item_update()
                courier_name = get_courier_name()
                courier_number = validate_phone_number()
                update_courier(item_selection, courier_name, courier_number)
            
            elif  couriers_menu_choice == "4":
                #delete item
                show_couriers_table()
                selection_item = select_item_delete()
                delete_courier(selection_item)
            
            else:
                print("Invalid entry detected, returning to couriers menu")
                
    elif main_menu_choice == "3":
        orders_menu_on = True
        while orders_menu_on:
            orders_menu()
            
            orders_menu_choice = input("Please enter a number listed above, or type 'Exit' to quit: ").title()
            
            if orders_menu_choice == "0" or orders_menu_choice == "Exit":
                #return main menu
                print("Returning to main menu")
                orders_menu_on = False
            
            elif orders_menu_choice == "1":
                #show current data
                show_current_list(orders)
            
            elif orders_menu_choice == "2":
                pass # enter item
                customer_name = get_customer_name()
                customer_address = get_customer_address()
                customer_number = validate_phone_number()
                show_products_table()
                basket = get_customer_orders()
                #show_couriers_table()
                customer_courier = get_customer_courier()
                make_new_order(orders, customer_name, customer_number, customer_address,\
                    customer_courier, basket)
                
            elif orders_menu_choice == "3":
                pass# update order status
                show_current_list(orders)
                order_index_value = input("Please enter the ID of the order would you like to edit: ")
                show_current_list(orders_status)
                orders_status_index = input("Please enter the ID of the status you'd like to set: ")
                update_order_status(orders, orders_status, orders_status_index, order_index_value)
                
            elif orders_menu_choice == "4":
                # update order
                show_current_list(orders)
                selected_list = input("Please input the ID of the order you'd like to edit: ")
                update_order(orders, selected_list)
            
            elif orders_menu_choice == "5":
                show_current_list(orders)
                remove_item = input("Please enter the ID of the item you wish to delete: ")
                delete_order(orders, remove_item)
            else:
                print("Invalid entry detected, returning to orders menu")
        
    else:
        print("Invalid entry detected, returning to main menu")
