from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=100)
    age = models.TextField()

