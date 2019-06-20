from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    schools =   models.CharField(max_length=30, default="")
    occupation = models.CharField(max_length=30, default="")
    branch = models.CharField(max_length=30, default="")
    listed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
