"""Hof funciones dentro de funciones"""


#### llamamos a una funcion dentro de otra funcion para acceder a su valor 

# def increment(a):
#     return a+1

# def higth_ord_func(x, func):
    
#     return x + func(x)

# result = higth_ord_func(2, increment)

# print(result)




# ==============>Prueba hof funcion  <============

def sumvalues(x):
    return x * 2
# este retorna 4

            #decimos que recivimos una funcion como parametro
def suma6(x, func):
    total = x*1     #usamos el valor que retorna la funcion
    total = total + func(x)
    return total
                    # declaramos la funcion que vamos usar
sumtotal = suma6(2,func=sumvalues)
print(sumtotal)