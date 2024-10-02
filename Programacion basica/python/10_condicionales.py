"""Condicionales """

# Nota: Nos sirven para verificar si algo se cumple o no 
"""ejempleficaremos un caso en el cual si un estudiante pasa o no pasa la materia cuando su nota sea
18 y el maximo es de 20 y el minimo es de 16

"""

is_active= False

student= 18
min= 16
max= 20



if is_active:
    print("El estudiantes esta activo ")
    if student >= min and student<=max:
        print(f"pasaste la materia con {student}") 
    else:
        print("perdiste")

else:
    print("el estudinate no esta activo ")


"""RETO PLATZI"""
import random

"""Crea un programa del calsico juego de piedra pepel o tijera y agrega un contador de perdidas y ganancias"""

stone:str = "piedra"
paper:str = "papel"
scissors:str = "tijera"


win:int = 0 
lost:int= 0

while win<3 and lost<3 :

    listvar =[stone, paper, scissors]
    optiona_random = random.choice(listvar) 

    player1 = stone
    boot = optiona_random


    if player1 == boot:
        print("Empate")

    if player1==stone and boot==scissors:
        win = win+1
        print( "Ganaste")
    elif player1==paper and boot == stone:
        win = win+1
        print("Ganaste")
    elif player1==scissors and boot== paper:
        win = win+1
        print("Ganaste")
    else: 
        print("Perdiste")
        lost = lost+1

print(f"ganaste {win} y perdiste {lost}")
if win >=3:
    print("tu ganas!!!") 
else:
    print("Tu pierdes!!!")