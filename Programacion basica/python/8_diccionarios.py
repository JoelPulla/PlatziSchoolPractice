
"""Diccionarios"""

#Nota: Son datos tipos llave Valor 

dic_new = {
    "name": "Joel Pulla",
    "Nick_name": "Joel25",
    "age" : 25,
    "life": True
}

print(dic_new)
print(dic_new["age"]) #impirmimos dato espesifico
del dic_new["age"]
print(dic_new)

print(type(dic_new.keys())) #saber tipo de datos de las llaves
print(dic_new.keys()) #imprime solo las llaves


print(dic_new.values()) #devulve solo los valores

print(dic_new.items()) #devulve en tupla los datos

# Crearemos una genda para ejemplificar esto 

ageda = {

    "Joel": {
        "Nick_name": "Joel25",
        "age" : 25,
        "life": True
    },
    "Fernanda":{

        "Nick_name": "JuanaBanana",
    "age" : 25,
    "life": True
    }

}

print(ageda["Joel"])