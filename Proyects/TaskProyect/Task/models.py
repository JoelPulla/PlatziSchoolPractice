from django.db import models

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True)
    done = models.BooleanField(default=False, verbose_name="Hecho")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

