"""Operaciones matematicas"""

a:int = 10 
b:int = 5

a+b # suma
a-b # resta
a*b # multiplicacion
a**b # Potenciacion  
a/b # division 
a%b #modulo o residuo
a//b # divicion con resultado entero 

a += 2 #asignacion 

""" Cuando tenemos varias operaciones dentro de una misma linea devemos aplicar el metodo pendas
    el cual nos permite dar un orden a las operaciones matematicas PEMDAS
    P potenciacion 
    E exponeciacion
    M matematica
    D division 
    A adicion
    S sustraccion
"""

a-(a*b)/2 #en este caso primero se ejecutara lo de los parentecis respetando el metodo pemdas 