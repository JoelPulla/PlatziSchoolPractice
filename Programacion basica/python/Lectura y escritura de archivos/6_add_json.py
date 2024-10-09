import json

add_json = {
            "name": "Juana Banana",
            "release_date": "1994-06-15",
            "rental_price": 56,
            "tax": 2.00,
            "rental_duration_hours": 48,
            "genre": "Animation",
            "available": True
        }
    

path_json = "Programacion basica/python/Lectura y escritura de archivos/example.json"


with open(path_json, mode='r') as file:
    movies = json.load(file) 
    
movies.append(add_json) #agrega a la lista

with open(path_json, 'w') as file:
    json.dump(movies, file, indent=4 ) #cobre escribre todo