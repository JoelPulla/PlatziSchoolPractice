""" Exepciones"""

#Nota: nos sirven para el manejo de erroes
    
while True:
    try:
        divisor = int(input("Ingresa el numero a dividir: "))
        res = 100 / divisor
        print (res)
    except ZeroDivisionError as e:
        print(f"No puedes dividir para 0, error: {e} ")
    except ValueError as e:
        print(f"No puedes dividir para string , error {e}")