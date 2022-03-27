from Library import *

print("""
****************************
WELCOME TO OUR DIGITAL LİBRARY

1.ALL BOOKS

2.SEARCH BOOKS

3.ADD BOOK

4.REMOVE BOOK

5.ADD PAGES TO A BOOK

6.SEARCH AUTHOR

!!!!! TO QUİT PRESS "Q" !!!!!
****************************
""")


library1 = Library()

while True :
    x = input("What do you want to do  ?")

    if x == "Q":
        print("Quitting from the library...")
        time.sleep(2)
        print("Good Bye...")
        break
    elif x == "1" :
        library1.showbooks()
    elif x == "2" :
        nam = input("Which book do you want to search")
        print("Searching Book...")
        time.sleep(2)
        library1.lookbook(nam)
    elif x == "3" :
        n = input("Book Name:")
        a = input("Author Name:")
        t = input("Type:")
        p = input("Publisher Name:")
        pa = input("Number of Pages:")

        bookn = Books(a, n, t, p, pa)
        print("Adding book...")
        time.sleep(2)
        library1.addbook(bookn)
        print("Book has been added.")

    elif x == "4" :
        r = input("Which book do you want to remove ?")
        print("Removing book...")
        time.sleep(2)
        library1.removebook(r)
        print("Book has been removed.")
    elif x == "5" :
        ap = input("Which book do you want to add page to ?")
        print("Adding a page...")
        time.sleep(2)
        library1.addpages(a1p)
        print("Page has been added.")
    elif x == "6" :
        au = input("Which author do you want to search")
        print("Searching Author...")
        time.sleep(2)
        library1.lookauthor(au)
        print("Author has been found.")
    else :
        print("There no such button, try another one.")
        continue

