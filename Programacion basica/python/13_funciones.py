
"""Funciones """

# sirven para reducir el codigo y hacerlo mas legible ademas su funcion 
# principal es reutilizar el codigo 

# palabra reservada 
def gret(name, age, locality="None"): #creo la funion y recivo un parametro 
    print(f"Hello {name} tu edad es {age} tu direccion es {locality}") #imporimo

gret("Joel Pulla", 21, "None")#llamo a la funcion 
gret("Marco", 25)
gret(locality="NY",age=26,name="Juana Banan")

############### Funcion matematica ##############33333

def fun_pot(a,b):
    return a** b

def fun_multi(a,b):
    return a *b

def fun_res(a,b):
    return a - b

def fun_sum(a,b):
    return a +b 


print (fun_sum(100,50)) 

################### Mejorare el codigo de platzi #############3###

# Ejercicio: Crear un calculadora usando funciones y que sean de ocion multible para el susaurio 

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multipli(a,b):
    return a * b

def divici(a,b):
    return a / b

    

def option():

    print(" ############ escoje una opcion #########")
    print("1 para suma")
    print("2 para resta")
    print("3 para multiplicacion")
    print("4 para divicion")
    print("5 para salir")

    respuesta = input("ingresa tu opcion: ")
    return respuesta

def calculador(dato_a, dato_b):
    respuesta = option()

    match respuesta:
        case _ if respuesta == "1":
            return(suma(a=dato_a, b=dato_b))

        case _ if respuesta == "2":
            return (resta(a=dato_a, b=dato_b))

        case _ if respuesta == "3":
            return (multipli(a=dato_a, b=dato_b))
        
        case _ if respuesta == "4":
            return (divici(a=dato_a, b=dato_b))
        
        case _ if respuesta == "5":
            return "Fin de la operacion"

respuesta = calculador(10, 20)
print(f"############## RESPUESTA = {respuesta} ##################")

