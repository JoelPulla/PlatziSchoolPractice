class Car:
    def __init__(self, id, model, age, price):
        self.id = id
        self.model = model
        self.age = age
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El carro {self.model} del año: {self.age} ha sido vendido por un valor de {self.price}")
        else:
            print(f"El carro {self.model} no está disponible")
    
class User:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
        self.cars = []
        
    def buy_sell(self, car):
        if car.available:
            car.sell()
            self.cars.append(car)
        else:
            print("No se pudo realizar la compra.")
                
    def consult(self, car, dealership):
        price = dealership.consult_price(car)
        if price is not None:
            print(f"El precio del carro {car.model} es: {price}")
        else:
            print(f"El carro {car.model} no está disponible en la concesionaria.")
        
class DealerShip:
    def __init__(self, name):
        self.name = name
        self.cars = []
        
    def add_cars(self, car):
        self.cars.append(car)
        print(f"El carro {car.model} ha sido agregado")
        
    def consult_price(self, car):
        for c in self.cars:
            if c.id == car.id:
                return c.price
        return None  # Retorna None si el carro no se encuentra

# Creación de instancias
car1 = Car(id=1, model="Toyota Prado", age="2024", price=40000)
car2 = Car(id=2, model="Ford 150", age="2020", price=60000)
car3 = Car(id=3, model="Chevrolet Colorado", age="2024", price=30000)

user1 = User(id=1, name="Joel Pulla")
user2 = User(id=2, name="Marco Antonio")
user3 = User(id=3, name="Juana Banana")

dealership1 = DealerShip(name="Importadora Tomebamba")  
dealership1.add_cars(car1)
dealership1.add_cars(car2)
dealership1.add_cars(car3)

# Consultar el precio del carro
user1.consult(car1, dealership1)

# Comprar el carro
user1.buy_sell(car1)
