"""Manejo de archivos .TXT"""

#leer linea por linea
"""with open('Programacion basica/python/POO/example.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""
        
#leer en una lista

"""with open('Programacion basica/python/POO/example.txt', 'r') as file:
    lines = file.readlines()
    print(lines[4:8])"""
    
#Esribir al final del archivo
"""with open('Programacion basica/python/POO/example.txt', 'a') as file:
    file.write('\n\n Escrtio por Chatgpt y promteado por Joel')"""
    
#Sobre escribir texto eliminadno el anterior 
"""with open('Programacion basica/python/POO/example.txt', 'w') as file:
    file.write('\n\n Escrtio por Chatgpt y promteado por Joel')"""
    

#### Reto para crear un contador de lines del archivo 
with open('Programacion basica/python/POO/example.txt', 'r') as file:
    row = 0
    for i in file:
        row = row +1
    
    print(f"total de linesas {row}")
    
    
# =====> Optimizacion <=====

with open('Programacion basica/python/POO/example.txt', 'r') as file:
    lines = file.readlines()
    print(f"Total de lines en tu archivo es {len(lines)}")