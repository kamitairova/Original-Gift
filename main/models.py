from django.db import models


class Cards(models.Model):
    image = models.ImageField(upload_to='CardIco')
    title = models.CharField(max_length=32, unique=True)
    list = models.CharField(max_length=15)
    text = models.TextField(max_length=25)
    cost = models.TextField(max_length=25)

    def __str__(self):
        return f"карточка: {self.title}|{self.text}: {self.cost}"






