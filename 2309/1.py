<<<<<<< HEAD

class Reader():
    books = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def take_book(self, book):
        if len(self.books) < 2:
            self.books.append(book)
        else:
            print('Too much')

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)


r = Reader('John', 'Connor', 14)
r.take_book('Kitchen')
r.take_book('Floor')
r.take_book('Monster')
print(r.books)
=======
class Reader():
    books = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def take_book(self, book):
        if len(self.books) < 2:
            self.books.append(book)
        else:
            print('Too much')

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)


r = Reader('John', 'Connor', 14)
r.take_book('Kitchen')
r.take_book('Floor')
r.take_book('Monster')
print(r.books)
>>>>>>> 0def721a1bfddc42d2f44c5238d7d3c5727dba3b
