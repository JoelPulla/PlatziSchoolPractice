# """ Recursividad """

# # Nota: Un programa se llama a si mismo para resolver un problmea 

# ###### Factorial de un numero es cundo multiplicampos por el numero siguienete
# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

# ##### Fibonacci ### 

# def fibonacci(n):
#     if n == 0:  
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(n=5))

# Funcion para cargar la suma de numeros naturales #

def sum_naturales(n):
    if n == 0:  
        return 0
    else:
        return n + sum_naturales(n-1)

print(sum_naturales(5))