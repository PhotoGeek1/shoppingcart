shopping_list = {"Target": ["socks", "soap", "detergent", "sponges"],
                "Safeway": ["butter", "cake", "cookies", "bread"],
                "PeterGrocery": ["apples", "oranges", "bananas", "milk"],
                "JaneGrocery": ["oreos", "brownies", "soda"]
                }


# main function
# raw input menu items
# if statements based on raw input, call functions

def main():
    while(True):
        option = int(raw_input('Enter the menu number you would like to execute:\n \
            0 = Main Menu \n \
            1 = Show all lists \n \
            2 = Show a specific list \n \
            3 - Add a new shopping list. \n \
            4 - Add an item to a shopping list. \n \
            5 - Remove an item from a shopping list. \n \
            6 - Remove a list by nickname. \n \
            7 - Exit when you are done. '))
        if option == 0: 
            main()
        elif option == 1:
            show_all_lists()
        elif option == 2:
            show_specific_list()
        elif option == 3:
            new_shopping_list()
        elif option == 4:
            add_item_to_shopping_list()
        elif option == 5:
            remove_item_from_shopping_list()
        elif option == 6:
            remove_store_list()
        else:
            break




# create main menu fuction to refresh menu
#     call main function

# create show all lists function
#     use for key, vlaue in shopinglist.items() to iterate through and print shopping list
def show_all_lists():
    for key, value in shopping_list.items():
        print key, value


# create show specific list function
#     use shoppinglist.keys() to show all shopping lists, ask user to input which list to view
def show_specific_list():
    list_name = raw_input("Which store's shopping list would you like to view? ")
    print shopping_list[list_name]


# create add new shopping list function
#     ask user for store name to use as key
#     ask user for shopping list items to store as value in key
def new_shopping_list():
    store_name = raw_input("What store would you like to create a shopping list for? ")
    new_store_items = raw_input("What items would you like to buy at this store? ")
    new_store_items_list = new_store_items.split(", ")
    shopping_list[store_name] = new_store_items_list
    print shopping_list[store_name]


# create add item to existing shopping list function
#     ask user which shopping list to add to
#     user to input value - append to existing values
def add_item_to_shopping_list():
    store_name = raw_input("Which store would you like to buy an item from? ")
    item_to_buy = raw_input("What item would you like to buy? ")
    get_list = shopping_list[store_name]
    get_list.append(item_to_buy)
    print shopping_list[store_name]


# create remove item from shopping list function
#     ask user which store to remove item from
#     ask user which item to remove from store list
def remove_item_from_shopping_list():
    store_name = raw_input("Which store would you like to remove an item from? ")
    item_to_remove = raw_input("What item would you like to remove? ")
    get_item = shopping_list[store_name]
    get_item.remove(item_to_remove)
    print shopping_list[store_name]


# create remove a list by nickname function
#     ask user which store to remove
def remove_store_list():
    store_name = raw_input("Which store would you like to remove? ")
    del shopping_list[store_name]
    print shopping_list

# create exit when done function
#     break out of program



if __name__ == '__main__':
    main()


