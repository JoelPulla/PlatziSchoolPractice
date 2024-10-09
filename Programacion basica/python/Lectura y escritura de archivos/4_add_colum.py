import csv

file_path = "Programacion basica/python/Csv/products.csv"
file_update = "Programacion basica/python/Csv/products_update.csv"


with open(file_path, 'r') as file:
    cvs_reader = csv.DictReader(file)
    
    #obetner el nombre de las columnas existentes y agregar 1 +
    fieldnames= cvs_reader.fieldnames + ['total_value']
    
    with open(file_update, mode='w',newline='' ) as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #escribe encabezado
        
        for row in cvs_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)