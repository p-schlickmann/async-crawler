import webbrowser
from scraper.async_books import all_books

i = 1000
for book in all_books:
    book['number'] = i
    i = i - 1
    if book['rating'] == 'One':
        book['rating'] = 1
    elif book['rating'] == 'Two':
        book['rating'] = 2
    elif book['rating'] == 'Three':
        book['rating'] = 3
    elif book['rating'] == 'Four':
        book['rating'] = 4
    elif book['rating'] == 'Five':
        book['rating'] = 5
    book['name'] = book['name'].title()


def book_page():
    while True:
        user_inp = input("""
<you can access the book page by entering it's number> 
  <or go back to the Filtering Menu pressing enter>
   
-> """)
        if user_inp == '':
            break
        try:
            user_int = int(user_inp)
        except ValueError:
            print("\n<please enter a valid book number! ex: 2>")
            continue
        for book in all_books:
            if user_int == book['number']:
                webbrowser.open(book['link'])
                print(f"\n<book {user_int} displayed on Chrome>")
                break
            elif user_int == 0 or user_int > 1000:
                print(f"\n<there are no books with that number, min-1 max-1000>")
                continue
        break


def print_book(book):
    print(f"""
        [{book['number']}]

{book['name']} 
Topic: {book['topic']}

    Stars: {book['rating']}
    Price: {book['price']}
____________________________________________________________""")


def list_all():
    for book in reversed(all_books):
        print_book(book)
    while True:
        user_inp = input("""
<you can access the book page by entering it's number> 
  <or go back to the Main Menu pressing enter>

-> """)
        if user_inp == '':
            break
        try:
            user_int = int(user_inp)
        except ValueError:
            print("\n<please enter a valid book number! ex: 2>")
            continue
        for book in all_books:
            if user_int == book['number']:
                webbrowser.open(book['link'])
                print(f"\n<book {user_int} displayed on Chrome>")
                break
            elif user_int == 0 or user_int > 1000:
                print(f"\n<there are no books with that number, min-1 max-1000>")
                break
        break


def my_filter():
    while True:
        user_c = input("""
______________________________________________________       
                <Filtering Menu>
    
Enter:
    
- 'p' to filter by price
- 'r' to filter by rating
- 'n' to filter by name
- 't' to filter by topic
- 'm' to go to the Main Menu
    
-> """)
        if user_c == 'p':
            while True:
                user_x = input("""
 <enter 'm' for the maximum book price you want>
 <enter 's' for a specific book price you want>
<or go back to the Filtering Menu pressing enter>

-> """)
                if user_x == '':
                    break
                user_p = input('\nPrice: ')
                try:
                    user_pfloat = float(user_p)
                except ValueError:
                    print("\n<please enter a valid price! ex: 13.99>")
                    continue
                t = 0
                if user_x == 'm':
                    for book in reversed(all_books):
                        if float(book['price']) <= user_pfloat:
                            print_book(book)
                            t = 1
                    if t == 0:
                        print(f"\n<no books were found below {user_pfloat}\n>")
                        continue
                    elif t == 1:
                        book_page()
                        break
                if user_x == 's':
                    for book in reversed(all_books):
                        if float(book['price']) == user_pfloat:
                            print_book(book)
                            t = 1
                    if t == 0:
                        print(f"\n<no books were found with {user_pfloat}>\n")
                        continue
                    elif t == 1:
                        book_page()
                        break

        elif user_c == 'r':
            while True:
                user_p = input("""
    <enter the number of stars you want>
<or go back to the Filtering Menu pressing enter>

-> """)
                if user_p == '':
                    break
                try:
                    user_int = int(user_p)
                except ValueError:
                    print("\n<please enter a valid book rating! ex: 2>")
                    continue
                t = 0
                for book in reversed(all_books):
                    if book['rating'] == user_int:
                        print_book(book)
                        t = 1
                if t == 0:
                    print(f"\n      <no books were found with {user_int} stars>")
                    continue
                elif t == 1:
                    book_page()
                    break

        elif user_c == 'n':
            while True:
                user_name = input("""
<enter the book name you want to find> 
<or go back to the Filtering Menu pressing enter>

-> """)
                if user_name == '':
                    break
                user_title = user_name.title()
                t = 0
                for book in reversed(all_books):
                    if book['name'] == user_title:
                        print_book(book)
                        t = 1
                if t == 0:
                    print(f"\n<no books were found with the name {user_title}>")
                    continue
                elif t == 1:
                    book_page()
                    break


        elif user_c == 't':
            while True:
                user_topic = input("""
What Topic you want to filter from?

Travel, Mystery, Historical Fiction, Sequential Art, Classics
Philosophy, Romance, Womens Fiction, Fiction, Childrens, Religion
Nonfiction, Music, Default, Science Fiction, Sports and Games, Add a comment
Fantasy, New Adult, Young Adult, Science, Poetry, Paranormal, Art
Psychology, Autobiography, Parenting, Adult Fiction ,Humor, Horror
History, Food and Drink, Christian Fiction, Business, Biography, Thriller
Contemporary, Spirituality, Academic, Self Help, Historical, Christian
Suspense, Short Stories, Novels, Health, Politics, Cultural, Erotica, Crime

<or if you want to go back to the Filtering Menu press enter>

-> """)
                if user_topic == '':
                    break
                else:
                    user_t = user_topic.title()
                    t = 0
                    for book in reversed(all_books):
                        if book["topic"] == user_t:
                            print_book(book)
                            t = 1
                    if t == 0:
                        print(f"\n<no books found with the topic '{user_t}'>")
                        continue
                    elif t == 1:
                        book_page()
                        break

        elif user_c == 'm':
            break

        else:
            print("\n<unknown command!>\n")
            continue
