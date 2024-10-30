# COFFEE CHOP 
Este es un proyecto funcional de una tienda de cafes, creado para practicar mis conocimientos en el FrameWork Djando 

## Guia para crear el proyecto desde 0 
>[!NOTE]
> Este proyecto fue creado en base al curso de paltzi 
> Utilizamos el sistema operattivo MacOs por lo que los comando son diferentes en Windos o Linux 

1. Crear el entorno virtual 
`python3 -m venv .vevnv` #crear
`source venv/bin/activate` #inicializa

2. Instala la despendencias 
`pip3 install Django` # instala Django 

3. Crea el archivo de dependencias
>[!IMPORTANT]
>Debes actualizar este proyecto en caso que instales mas librerias 
`pip freeze > requirements.txt`

4. crea el proyceto y aplicaciones 
`django-admin startproject coffe_shop .` #Crea el proycetro en principio 
`django-admin startapp products` # Crea la app de productos 
>[!IMPORTANT]
>Debes vincualar las apps al proyecto principal en Settings

7. Crea las reglas de negocio y realiza las migraciones 
`python manage.py makemigrations` crea la migracion 
`python manage.py migrate` migra los cambios a la BDD

8. Crea los fomrularios en un archivo forms.py en la aplicacion

- Debes crear la funcion con el metodod objets.create(aqui debes pasar la data)
## Librerias Nativas Django 

9. crea las vistas 
- "Forms" Para crear Formularios de Djando 
`Form djando import forms` 



## Librerias de terceros  
> ### Pillow 
> Se encarga de realizar validaciones de las imagenes que se suben a la BDD
