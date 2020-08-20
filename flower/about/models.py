from django.db import models

# Create your models here.
class about(models.Model):
    Description=models.CharField(max_length=300)


    def __str__(self):
        return self.Description

