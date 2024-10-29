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
