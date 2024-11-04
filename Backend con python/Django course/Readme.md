# Curso de Djnago 

Este es un curso basico del uso del Frameword Django para desarrollo web y backend con 
python este framwork es de codigo abierto, fue creado para el desarrollo de blogs

para empezar debemos tener en cuenta dos cosas este nos sirve para desarrollo web 
si envargo di deseamos concetarnos a varias aplicaciones simultaneamente debemos usar 
una api rest para para ello se debe agrgar el otro paquete de django "Django Rest Framework" pero eso lo veremos en otro curso 

## Como Empezar

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
`python manage.py migrate` envia los cambios a la BDD 


9. Verifica que en que BDD estan guardandose los datos
`./manage.py dbshell`

10. Inserta datos mediante la sell de Django 
`python manage.py shell`

```
#Importa las dependecias

from my_first_app.models import Car

#Crea una instancia 
car_1 = Car(title ="Ford", year = "2022")

#define una funcion para la lectura de los datos que escribiste 

def __str__(self):
    return f"{selft.title} - {self.yaer} "

print(car_1)

#envia a la bdd con el metodo save()

car_1.save()

```
11. Elimina Datos 
- Solo demes usar el metodo .delete() y es todo 

12. Agregar mas datos a un modelo 
- Una vez agregas los nuevos datos debes hacer la migracion 
    - `python manage.py makemigrations "app(opcional)"` # crea la migracion pero no la ejecuta si recives un error debes solucionar aqui 
    - `python manage.py migrate "app(opcional)"` # ejecuta y aplica la migracion y crea los datos 

13. Agregar datos mediante terminal 

`python manage.py shell`

14. Eliminar datos mediante Terminar 
`DELETE  FROM my_first_app_car WHERE id == 1;`

- Para crear datos debes importar los modelos y luego debes usar el metodo save

```
from my_first_app.models import Project, Task

p = Project(name= "Proyecto1" )
p
p.save()
```

## Interactura con la BDD
- Actualizacion 
> Selecciona la shell de BDD `python manage.py dbsell`

`.tables` - Muestra las bases de datos disponibles 

`SELECT * FROM my_first_app_car` - Muestra todos los datos en la tabla espesificada
`SELECT * FROM my_first_app_car WHERE id == 1` - Selecciona uno en espesifico 

14. Cunado creamos un app Utilizamos la arquitectura mvt para poder utilizar todo primero debemos agregar nuestra aplicacion a nuestro proyecto y depues crear el html 

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



# Ejemplo de codigo con realaciones en los modelos 

```

from django.db import models

# Create your models here.
# Sistema de libros
class Publisher(models.Model):  
    name = models.CharField(max_length=100)  
    address = models.CharField(max_length=80)  
    
    def __str__(self):
        return self.name

class Author(models.Model): 
    name = models.CharField(max_length=50)  
    birth_date = models.DateField()  
    
    def __str__(self):
        return self.name
    
# Uno a Uno 
class Profile(models.Model):
    
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(500)

# Muchos a Muchos
class Book(models.Model):
    title = models.CharField(max_length=50) 
    published_date = models.DateField()
    
    # Uno a muchos: Una editorial publica muchos libros
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  
    
    # Muchos a muchos: Un libro puede tener varios autores y viceversa
    authors = models.ManyToManyField(Author, related_name='authors')  
    
    def __str__(self):
        return self.title

```

# Manager 

- Se usa dentro de las shell

    `Author.objects.count()` saber cuantas registros hay 
    `Author.objects.first()` Trae el primer reghistro 
    `Author.objects.last()`  Ultimo registro enviado a la BDD
    `Author??` me muestra las propiedades de la clase 
    `Author.objects.all()` me trae todos los registros 
    `Author.objects.filter(name = "JoelDev")` filtra datos con asignacion no comparacion 
    `Author.objects.filter(name = "JoelDev").delete()` Elimina el dato que encontro con el filtro 
    `Author.objects.order_by("name")` Ordena por el objeto que le enviamos en orden alfabetico ß


# Gestion de Urls 

- Para mejorar la gestion es poner cada url aislada por aplicacion es un archiuvo urls.py
es como nuestro archivo de barril de DART

- lo llamamos desde el urls del proyecto principal 
- si deseamos agregar un parametro para neustra fuinciones debe ser los siguiente 
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('app_cars.urls'))
    path('carros/detalle/<int:id>/', include('app_cars.urls'))
]

```
