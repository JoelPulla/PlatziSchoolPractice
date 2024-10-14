"""Hof funciones dentro de funciones"""


# def increment(a):
#     return a+1

# def higth_ord_func(x, func):
    
#     return x + func(x)

# result = higth_ord_func(2, increment)

# print(result)




# ==============>Prueba hof funcion  <============

def sumvalues(x):
    return x * 2



def suma6(x, func):
    total = x*1
    total = total + func(x)
    return total

sumtotal = suma6(2,func=sumvalues)
print(sumtotal)