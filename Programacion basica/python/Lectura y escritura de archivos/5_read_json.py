import json 

path_json = "Programacion basica/python/Lectura y escritura de archivos/example.json"

with open(path_json, 'r') as file:
    movies = json.load(file) # lee
    # print(movies) # mostrar contenido]
    
    for movie in movies:
        # print(i) #devulve so˚lo dic 
        print(f" ====> movie {movie['name']} su estado es {movie['available']} <===")