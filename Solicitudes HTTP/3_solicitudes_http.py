""" Solicitudes HTTP"""

# cosumimos datos de internet con la libreria 
#"pip3 install requests" 

import requests

def get_categories():
    query = requests.get('https://api.escuelajs.co/api/v1/products')
    
    print(query.status_code)
    # print(query.text)
    
    categoryes = query.json()
    for product in categoryes:
        print(product['price'])
    
get_categories()