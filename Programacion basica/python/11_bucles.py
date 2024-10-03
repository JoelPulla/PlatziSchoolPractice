
numbers = [1,2,3,4,5,6]

for i in numbers: #recorre i en numbers
    print(i) #imprime el valor de i

for i in range(0,10): # recorre i en un rango 
    print(i+1)


fruits = ["Manzana", "Pera", "Perita", "Manzanita", "mango,"]

for fruit in fruits:
    print("no es la fruta que buscas")
    if fruit == "Perita":
        print(f"Encontramos a {fruit}")

# ###########3 While ##########
# While en español es como mientra en esete caso se puede usar don de necesitamos 
# recorer miestras una condicion se cumple no no


x= 0 

while x<5: #recorre hasta que x valga 5
    x +=1

    if x== 3:
        # break # detine el ciclo
        continue # omite esta parte del codigo 
    
    print(x) 
