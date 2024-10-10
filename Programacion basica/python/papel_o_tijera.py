import random

"""Crea un programa del clasico juego de
 piedra pepel o tijera y agrega un contador de perdidas y ganancias"""

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