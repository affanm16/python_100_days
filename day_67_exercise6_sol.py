"""
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods.
 Show that your program doesn't persist the books after the program is stopped!

"""
class Library:
    def __init__(self):#constructor which declares no.of books variable and list of books
        self.no_of_books=0
        self.books=[]#empty list
    def addBook(self,book):#add books to the library
        self.books.append(book)
        self.no_of_books=len(self.books)
    def showInfo(self):
        print(f"the library has {self.no_of_books} books ")
l1=Library()
l1.addBook("Harry puttar1")
l1.addBook("Harry puttar2")
l1.addBook("Harry puttar3")
l1.showInfo()
print(l1.books)
