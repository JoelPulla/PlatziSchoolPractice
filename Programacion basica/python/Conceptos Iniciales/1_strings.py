"""
 Tipode Variables en python 
"""

# String o cadenas de texto con el tipo 
name = "hola "
name_stric:str = "Mundo"

name_2:str = """
varibale que permite saltos de linea
y no afecta al resto del codigo 
"""

type(name) #TYPE no sirve para saber el tipo de dato

name[1] #imprimos la pocicion de un caracter
name + " "+ name_stric #Concatenacion de strings

len(name_stric) #cuantos caracteres tiene una variable
name.lower() #trasforma en minusculas
name.upper() #Transforma en mayusculas
name.capitalize() #Transforma la primera en mayuscula
name.title() #Transforma la primera en mayuscula
name.swapcase() #Transforma todas a mayuscula
# name.replace() #
name.split() #trasforma en una lista
# print(name.strip())
# name.lstrip() 
# name.rstrip() 
# name.find()
# name.index() 


""" f Format strings"""

a = (f"Hola {name} como estas, tu otro nombre es {name_stric}")