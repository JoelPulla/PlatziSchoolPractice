class Person:
    #Contructor: Es una funcion propia y especial de una clase en la cual defino nuestros atributos
    #para recivir los datos
    def __init__(selft, name,age):
        selft.name = name
        selft.age = age
    #metodo o funcion: ejecuta un proces0
    def greet(selft):
        print(f"Hola {selft.name} wow! tu edad es {selft.age}")
        
#Intancia: creamos una instancia la cual crea un objeto persona 1 y 2
person1= Person("Joel", 21)
person2= Person("Maria", 45)

#Persona llama a un metodo
person1.greet()
person2.greet()

###Banco 

class BancnkAcount():
    def __init__(self, number, titular, date):
        self.number = number
        self.titular = titular
        self.date = date
    
    def share(self):
        print(f"Has enviado un dinero de la cuenta: {self.number}, titular: {self.titular} el dia {self.date}")
    
    def data_consult(self):
        print(f"Hola {self.titular} por el momento no tienes dinero en tu cuenta: {self.number}, informe de {self.date}")
        

bankacount1 = BancnkAcount(2466, "Joel Pulla", "1 Febrero")
bankacount2 = BancnkAcount(3233, "Maria Matute", "30 de enero")

bankacount1.share()
bankacount2.data_consult()

#### Platzi Example ###

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self. balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")

    def withdraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

#Llamada a los metodos
account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)