# """Iteradores en entero """
# # ir iterando en cada elemento si utilizar indices

# my_list= [1,2,3,4]

# my_iter = iter(my_list)

# print( next(my_iter)) #ver los valores que se guardan en memoria
# print( next(my_iter)) 
# print( next(my_iter)) 
# print( next(my_iter)) 

# #itera solo en el valor de lo que tenemos pero no se sale de la lista 
# # por que ahi me arroja un error

# """Iteradores en cadenas de texto"""

# text = "Hello Word My Example"
# iter_var = iter(text)

# for i in iter_var: #  
#     print(i) 


# # """"""""""""""""""""""""""""

# #iterador para numero par 

# limit = 10       #start stop   step
# odd_itter = iter(range(0,limit+1,2))
#                 #inicia  limite  cuantas pociciones avanza

# for num in odd_itter:
#     print(num)

# ############################ GENERADOR ################################

# """ 

# Un generador en Python es una forma especial de crear iteradores que permite 
# generar valores sobre la marcha, en lugar de almacenarlos todos en memoria. 
# Los generadores utilizan la palabra clave yield en lugar de return. 
# Esto hace que una función se comporte como un generador, 
# lo que permite pausar su ejecución y reanudarla más tarde, conservando su estado.

# """

# def my_generador():
#     yield 1 #un generador funciona diferente ya que devuelve un valor similar a return 
#     yield 2 
#     yield 3 

# for data in my_generador():
#     print(data)


# # ####################33 Fibonaci Example ##########

# def fibonacci(limit:int):
    
#     a,b = 0,1 
#     while a < limit:
#         yield a
#         a ,b = b, a + b

# for num in fibonacci(10):
#     print(num)



######### genradores para numeros impares #########

def gen_impar(limit):
    a =1
    while a <= limit:
        yield a
        a = a+2 

for i in gen_impar(20):
    print(i)

def gen_par(limit:int):

    b = 2
    while b <= limit:
        yield b
        b = b+2

for i in gen_par(20):
    print(i)