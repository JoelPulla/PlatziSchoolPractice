"""Listas con sublistas MATRISES"""

#Nota: La podemos interpretar con filas y comlumas

matrix = [ [1,2,3,4,5], #fila 0
             [6,7,8,9,10], #fila 1
             [11,12,13,14,15] #fila 2
            ]
    #Columna 0  1  2  3  4  

print(matrix[1][0])

""" TUPLAS  """

#Nota: una tupla es immutable, si queremos realizar una funcion con un metodo no lo vamos a lograr
#      por que al ser inmutable no podemos modificar ningun dato

tuple_1 = (1,2,3,4,5,6,7,8,9)
print(type(tuple_1))
print(type(tuple_1[1])) #funcionan los datos internos con indexacion 