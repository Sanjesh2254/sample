from django.db import models

# Create your models here.
class Drink(models.Model):
    name=models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.Name



class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')