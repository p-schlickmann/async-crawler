from functions.my_functions import list_all, my_filter

options = """
___________________________________________________
                     <Main Menu>
    
Enter:
    
- 'l' to see all books
- 'f' to filter by price, rating, name or topic
- 'q' to quit
    
-> """

choice = {"l": list_all, 'f': my_filter}


def menu():
    user_choice = input(options)
    while user_choice != 'q':
        if user_choice in choice:
            choice[user_choice]()
        else:
            print("Unknown Command!")
        user_choice = input(options)


menu()
