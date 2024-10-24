# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */




def cal_area(tipo, altura_1= 0, base_1 = 0, base_2 = 0, altura_2 = 0):
    
    if tipo == "triangulo":
        print(( "Area de un triangulo es => ",(base_1 * altura_1)/2))
    elif tipo == "cuadrado":
        print( "Area de un cuadrado es => ",altura_1*altura_1)
    elif tipo == "rectangulo":
        print  ("Area de un rectangulo es =>",base_1 * altura_2)
    else:
        print("No reconozco ese calculo")
        


cal_area(

    tipo="cuadrado",
    altura_1= 34,
    altura_2=34
    
)

#### Mejora ###
def calcular_area(tipo, base=0, altura=0, lado=0):
    if tipo == "triangulo":
        area = (base * altura) / 2
        print(f"Área de un triángulo: {area}")
        return area
    elif tipo == "cuadrado":
        area = lado * lado
        print(f"Área de un cuadrado: {area}")
        return area
    elif tipo == "rectangulo":
        area = base * altura
        print(f"Área de un rectángulo: {area}")
        return area
    else:
        print("Polígono no soportado.")
        return None

# Ejemplos de uso:
calcular_area(tipo="triangulo", base=10, altura=5)
calcular_area(tipo="cuadrado", lado=4)
calcular_area(tipo="rectangulo", base=8, altura=6)
