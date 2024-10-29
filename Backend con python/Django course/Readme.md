# Curso de Djnago 

Este es un curso basico del uso del Frameword Django para desarrollo web y backend con 
python este framwork es de codigo abierto, fue creado para el desarrollo de blogs

para empezar debemos tener en cuenta dos cosas este nos sirve para desarrollo web 
si envargo di deseamos concetarnos a varias aplicaciones simultaneamente debemos usar 
una api rest para para ello se debe agrgar el otro paquete de django "Django Rest Framework" pero eso lo veremos en otro curso 

1. Para empezar debes innstlar el paquete de Django en un entrornoi virtural para aislar tu proyecto.

`python -m venv .venv` ".venv es el nombre de mi entorno virtual"

2. instala Django 
`pip install django`

3. Crea el proyecto mediante la termin al 
`django-admin startproject example1 .` "ten en cuenta que example1 es el nombre de mi proyecto, y el sigo . es para que se cree justo en la ubnicacion del sistema que estoy"

4. Levanta el servidor 
`python manage.py runserver` # ejecuta en un puerto por defecto
`python manage.py runserver 8080` #ejecuta en el puerto que espesifiquemos 

5. verifica si el server esta arriba en la direcion local de tu computador con el puerto 
que allas escojido 

`http://127.0.0.1:8000` 

6. Crear Una App 
`python manage.py startapp my_first_app` 

7. Migracion de base de datos
`python manage.py migrate` crea la base de datos basica para realizar autenticacion manejo de perimos etc  

8. Crea la base de datos segun tus modelos
`python manage.py makemigrations` crea la base de datos, segun los modelos 
9. Verifica que en que BDD estan guardandose los datos
`./manage.py dbshell`

10. Agregar mas datos a un modelo 
- Una vez agregas los nuevos datos debes hacer la migracion 
    - `python manage.py makemigrations` # crea la migracion pero no la ejecuta si recives un error debes solucionar aqui 
    - `python manage.py migrate` # ejecuta la migracion y crea los datos

7. Cunado creamos un app Utilizamos la arquitectura mvt para poder utilizar todo primero debemos agregar nuestra aplicacion a nuestro proyecto y depues crear el html 

- en los settings del proyecto agregamos el nombre de la app en `Installed App`, 

## Arquitectura de Django 

- MVT "Modelo Vista Templeate "

Modelo => Logia del neogocio 
Vista => Conector con los datoss y define desdo donde viene y sale 
Templeate => Es el fontend Html, Css

Modelo  envia la lista de productos ===> Vista recive y los pasas al templeate == templeate recive y dibuja los datos 

## Diferencia entre Proyecto y Aplicacion 

- Proyecto 
Este alverga todo aplicaicones estilos, modulos etc

- Aplicacion (App)
Este separa en modulos las funcionalidades para evitar que nuestro proyecto insostenible y para que sea de facil crecimeinto. 

# ORM Object Relational Maping

- Es una forma que permite esrcibir codigo en vez de sentencias sql mejorando la seguridad y evitando inyeccion de sql 

> Generalmente este proyecto se crea con sqllite que se usa para desarrollo mas no para producion ya que no esta diseñado para alta concurrencia

