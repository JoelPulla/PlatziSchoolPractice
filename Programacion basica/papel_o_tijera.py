"""Crea un programa del calsico juego de piedra pepel o tijera"""


stone:str = "piedra"
paper:str = "papel"
scissors:str = "tijera"

player1:str = stone
boot:str = paper


if player1 == boot:
    print("error empates")

if player1==stone and boot==scissors:
    print( "Ganaste: piedra rompe tijera")

if player1==stone and boot==paper:
    print("Perdiste: papel envuelve a piedra")


if player1==paper and boot == scissors:
    print("Perdiste: tijeras cortan papel")

if player1==paper and boot == stone:
    print("Ganaste: Piedra envuelve a papel")


if player1==scissors and boot==paper:
    print("Ganaste: Papel corta tijeras")

if player1==scissors and boot == stone:
    print("Perdiste: Piedra gana a tijera")