###Gestion de una biblioteca ###

#Gestion de una biblioteca "libro, Persona, Biblioteca"


class Book:
    def __init__(self, title, autor ):
        self.title = title
        self.autor = autor
        self.available = True
        
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} a sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")
        
    def return_book(self):
        self.available = True
        print(f"El libro {self.title } a sido devuelto")   
        
class User:
    def __init__(self,name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books= []
        
    def borrowed_book(self, book):
        if book.available:   
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"No puedes pedir {book.title}por que no esta disponible")
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro: {book.title} no esta en tu llista de prestados")
            

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_boks(self, book):
        self.books.append(book)
        print(f" El libro: {book.title} a sido agregado")
        
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} a sifo agregado ")
        
    def show_libraries(self):
        print("Libros disponibles")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.autor}")


user1 = User("Joel Pulla", 1)
user2 = User("Juana Banana", 2)

book1 = Book("Clean Code", "Algun representante")
book2 = Book("El principito", "Maria Amada")
book3 = Book("Iphone", "Steve Jobs")

library1 = Library()
library1.add_boks(book1)
library1.add_boks(book2)
library1.add_boks(book3)
library1.register_user(user=user1)

#mostrar libro 
library1.show_libraries()

#prestamo
user1.borrowed_book(book1)

#mostrar libro 
library1.show_libraries()

#devolver libro
user1.return_book(book1)

#mostrar libro 
library1.show_libraries()
