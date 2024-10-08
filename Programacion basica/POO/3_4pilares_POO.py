class Vehicle:
    def __init__(self, brand, model, price):
        
        ## Encapsulacion -- estos son datos privados
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avilable = True
    
    def sell(self):
        if self.is_avilable:
            self.is_avilable = False
            print(f"El vehiculo {self.brand}. ha sido vendido")
        else:
            print(f"El vehiculo{self.brand} no esta disponible")
    #Abstraccion 
    def check_avilable(self):
        return self.is_avilable
    #abstraccion
    def get_price(self):     
        return self.price
    
    def start_engine(self):
        raise NotImplemented("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplemented("Este metodo debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    
    #Polimorfismo: se basa en multifuncionalidad una isntacia obligatoria 
    def start_engine(self):
        if not self.is_avilable:
            return print(f"El motor del coche {self.brand} esta en marcha")
        else:
            return print(f"El coche {self.brand} no esta disponible")

    def stop_engine(self):
        if self.is_avilable:
            return print(f"El motor del coche {self.brand} se detenido")
        else:
            return print(f"No esta disponible el  motor del cohce {self.brand}")
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_avilable:
            return print(f"La bicicleta {self.brand} esta en marcha")
        else:
            return print(f"La bicicleta {self.brand} no esta disponible")

    def stop_engine(self):
        if self.is_avilable:
            return print(f"La bicicleta {self.brand} se detenido")
        else:
            return print(f"No esta disponible la bicicleta {self.brand}")
          

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_avilable:
            return print(F"El camion {self.brand} esta en marcha")
        else:
            return print(f"El camion {self.brand} no esta disponible")

    def stop_engine(self):
        if self.is_avilable:
            return print(f"El camion {self.brand} se detenido")
        else:
            return print(f"No esta disponible el camion {self.brand}")
    
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle:Vehicle):
        
        if vehicle.check_avilable():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            return print(f"Lo siento el viculo {vehicle.brand} no esta disponible")
    
    def inquiere_vehicle(self, veicle:Vehicle):
        if veicle.check_avilable():
            availablity = 'Disponible'
        else:
            availablity= 'No Disponible'
            
        print(f"El vehiculo: {veicle.brand} esta {availablity} y cuesta {veicle.get_price()}")
    
    
class DalerShip:
    def __init__(self, name):
        self.name = name 
        self.inventary = []
        self.customers = []
        
    def add_vecile(selft, veicle:Vehicle):
        if veicle.is_avilable:
            selft.inventary.append(veicle)
            print(f"El vehiculo {veicle.brand} a sido a;adido a la lista")
    
    def add_customer(seflt, customer:Customer):
        seflt.customers.append(customer)
        print(f"El cliente {customer.name} a sido agregado")
    
    def show_avilable_vehicles(self):
        print(f" ###### Estos son los vehiuclos disponibles en la tienda {self.name}  ########")
        for veicle in self.inventary:
            if veicle.check_avilable():
                print(f" Vehiculo {veicle.brand} disponible por {veicle.get_price()}")
                
                


car1 = Car(brand="Toyota",model= "Prado", price=20000  )
car2 = Car("Ford", "F150",  30000)
bike1 = Bike("Gocorp", "Feria", 1000)
bike2 = Bike("Coral", "For", 200)
truck1 = Truck("Foton", "Mediana", 80000)

customer1 = Customer("Joel Pulla")

dalership1 = DalerShip("Importadora Tomebamba")
dalership1.add_vecile(car1)
dalership1.add_vecile(car2)
dalership1.add_vecile(bike1)
dalership1.add_vecile(truck1)

dalership1.show_avilable_vehicles()

customer1.inquiere_vehicle(car1)

customer1.buy_vehicle(car1)

dalership1.show_avilable_vehicles()