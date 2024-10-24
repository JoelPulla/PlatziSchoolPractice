# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo:
#  *   https://avatars.githubusercontent.com/u/123515001?s=96&v=4
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */

from PIL import Image
import requests
import random

add_url = random.randint(1,1001)
add_url = str(add_url)+".png"
host = "/Users/joelpulla/software/platzi/PlatziSchoolPractice/100 ejercicios /others/"+add_url

#cal mcd

def cal_mcd(max, min):
    while min != 0:
        a = max % min
        max, min = min, a  # Actualiza max y min
    return max  # Devuelve el MCD


def aspect_radio(image_url):
    
    #donwland image 
    image = requests.get(image_url)
    if image.status_code == 200:
        with open(host, 'wb') as f:
            f.write(image.content)
            print(f"Donwland Correct in {host}")

    #data image
    image = Image.open(host)
    w,h = image.size
    
    #Llamada a la función
    resultado = cal_mcd(w, h)

    w = w//resultado
    h = h// resultado
    
    print(w,":",h)
    
    
    
aspect_radio("https://avatars.githubusercontent.com/u/123515001?s=96&v=4")

