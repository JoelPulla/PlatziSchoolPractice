"""Diccionario con map"""

#Podemos aplicar un map a una lista de diccionarios
#el map aplica alguna operacion que nosotros escribamos por cada elemnto drento de la lista

products = [
    {
        'product': 'camisa',
        'price': 50
    },
    {
        'product': 'pantalon',
        'price': 60
    },
    {
        'product': 'reloj',
        'price': 100
    }
    ]

## crea un programa que alamacene en una lista solo los precios

prices = list(map(lambda item: item['price'], products))
# print(prices)

## Reto con map agrega un atributo a cada dicionarion con los impuestos con el 0.15
def add_taxes(item):
    new_item = item.copy()
    new_item['taxe'] = new_item['price'] * .15
    new_item['total'] = new_item['price'] + new_item['taxe']
    
    return new_item

total = list(map(add_taxes, products))
print(total)
print(products)


# ================> inmutabilidad <=============

""" Se refiere a que mi diccionario inicial sufre un cambio en el espacio de memoria de mi 
    computadora lo que significa que si quiero acceder despues a ese espacio abria subido un cambio 
    con el metodo .copy() creo un nuevo dicionario al cual hacer los cambio y al final imprimo la nueva lista 
    y imprimo la vieja lista para saber cuales son los varoles neuvos y los viejos
"""