import sqlite3

import time

class Books():
    def __init__(self, author, book, type, publisher, pages):
        self.author = author
        self.book = book
        self.type = type
        self.publisher = publisher
        self.pages = pages

    def __str__(self):
        return "Book : {}\nAuthor : {}\nType : {}\nPages : {}\nPublisher :{}".format(self.book, self.author, self.type, self.pages, self.publisher)


class Library() :
    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()

        look = "Create Table If not exists BOOKS (author TEXT, book TEXT, type TEXT, publisher TEXT, pages INT)"
        self.cursor.execute(look)
        self.connection.commit()

    def cutconnect(self):
        self.connection.close()

    def showbooks(self):
        look = "Select * from BOOKS"
        self.cursor.execute(look)

        books = self.cursor.fetchall()

        if len(books) == 0 :
            print("There is not any books around this library.")
        else:
            for i in books:
                book = Books(i[0], i[1], i[2], i[3], i[4])
                print(book)
                print("************")

    def lookbook(self, book):
        look = "Select * from BOOKS where book = ?"
        self.cursor.execute(look, (book,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("Sorry there is not any book named like this.")
        else :
            book = Books(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def addbook(self, book):
        look = "Insert into BOOKS Values(?,?,?,?,?)"
        self.cursor.execute(look, (book.author, book.book, book.type, book.publisher, book.pages))
        self.connection.commit()

    def removebook(self, book):
        look = "Delete from BOOKS where book = ?"
        self.cursor.execute(look, (book,))
        self.connection.commit()

    def addpages(self,book):
        look = "Select * from BOOKS where book = ?"
        self.cursor.execute(look, (book,))

        books = self.cursor.fetchall()

        if len(books) == 0 :
            print("There is not any book named like this.")
        else :
            page = books[0][4]
            page += 1

            look2 = "Update BOOKS set pages = ? where book = ?"
            self.cursor.execute(look2, (page, book,))
            self.connection.commit()

    def lookauthor(self,author):
        look = "Select * from BOOKS where author = ?"
        self.cursor.execute(look,(author,))

        authors = self.cursor.fetchall()

        if len(authors) == 0 :
            print("There is not any author named like this")
        else :
            for i in authors:
                print("Author named {} wrote {}.".format(i[0], i[1]))






















