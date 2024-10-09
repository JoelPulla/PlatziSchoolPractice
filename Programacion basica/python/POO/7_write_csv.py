import csv

new_data = {
    'name':'book Air',
    'pricre':1300,
    'quantity':1,
    'brand': 'Mac',
    'category': 'Teconologia',
    'entry_Date': 'Jun-2024'
    
}

"""Insertar nuevas  """
with open('Programacion basica/python/POO/products (1).csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writr = csv.DictWriter(file,fieldnames= new_data.keys())
    csv_writr.writerow(new_data)