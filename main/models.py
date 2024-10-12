from django.db import models


class Cards(models.Model):
    image = models.ImageField(upload_to='static/images/')
    title = models.CharField(max_length=32, unique=True)
    list = models.TextField()
    text = models.TextField()
    cost = models.TextField(max_length=25)
