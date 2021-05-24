# --------------------------------------------------------- #
# Title: <Type the name of the script here>
# Description: <Type a description of the script>
# Name: Sara Tupponce
# Date: 05/24/2021
# Change Log:
#     STupponce - 05/24/2021 - created functions
#     STupponce - 05/24/2021 - created while loop to display to user
#     STupponce - 05/24/2021 - added error handling
# --------------------------------------------------------- #


import pickle

# -- Data -- #
item = ""  # str item to add to inventory
inventory = []  # list data to pickle
inventory_file = "pickle_inventory.dat"  # filename

# -- Processing -- #


def pickle_and_write_data(data, file_name):
    """Creates a binary file and writes pickled data do it

    param: list data
    param: file name to save data to
    """
    file = open(file_name, "ab")  # creates a binary file and opens in append mode
    pickle.dump(data, file)  # pickles and stores the data list in the file
    file.close()


def unpickle_and_read_data(file_name):
    """Reads data from file and un-pickles it

    param: file name to get data from
    return: str list (un-pickled data from file)
    """
    file = open(file_name, "rb")
    data = pickle.load(file)
    return data

# -- Presentation (I/O) -- #


def print_menu():
    """  Displays a menu of choices to the user"""

    print('''
    Menu of Options
    1) Add a new item to inventory
    2) Show inventory
    3) Save Data to File 
    4) Show Data in File       
    5) Exit Program
    ''')
    print()


def menu_choice():
    """ Gets the menu choice from a user

    :return: int
    """
    try:
        choice = int(input("Which option would you like to perform? [1 to 5] - "))
        print()
        return choice
    except ValueError:  # gives an error if the user does not enter a menu number choice
        print("Menu choice not recognized. Please select a menu option number 1-5")


# -- Main Body of Script -- #

while True:
    print_menu()
    user_choice = menu_choice()

    if user_choice == 1:  # add a new item to inventory
        item = str(input("Enter an item to add to your inventory: "))
        inventory.append(item)
    elif user_choice == 2:  # show inventory
        for item in inventory:
            print(item)
    elif user_choice == 3:  # save data to file
        pickle_and_write_data(inventory, inventory_file)  # pickles and saves data to file
        print("Data Pickled and Saved")
    elif user_choice == 4:  # show data in file
        unpickle_and_read_data(inventory_file)
        for item in inventory:
            print(item)
    elif user_choice == 5:  # exit program
        print("Exiting Program")
        break

