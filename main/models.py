from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



class Setting(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    subtitle_1 = models.CharField(max_length=50, blank=True, null=True)
    subtitle_2 = models.CharField(max_length=50, blank=True, null=True)
    title_image = models.ImageField(upload_to='banner', blank=True, null=True)

    is_active_cards = models.BooleanField(default=True)
    cards = models.CharField(max_length=50, blank=True, null=True)

    is_active_examples = models.BooleanField(default=True)
    examples = models.CharField(max_length=50, blank=True, null=True)

    is_active_offers = models.BooleanField(default=True)
    offers = models.CharField(max_length=50, blank=True, null=True)

    is_active_calendars = models.BooleanField(default=True)
    calendars = models.CharField(max_length=50, blank=True, null=True)

    is_active_reviews = models.BooleanField(default=True)
    reviews = models.CharField(max_length=50, blank=True, null=True)

    is_active_manual = models.BooleanField(default=True)
    manual = models.CharField(max_length=50, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.pk and Setting.objects.exists():
            raise ValidationError("You can only create one instance of Settings.")
        return super(Setting, self).save(*args, **kwargs)


# class Card_list(models.Model):
#     row_1 = models.CharField(max_length=50, blank=True, null=True)
#     row_2 = models.CharField(max_length=50, blank=True, null=True)
#     row_3 = models.CharField(max_length=50, blank=True, null=True)
#
# class CardListRelationship(models.Model):
#     card = models.ForeignKey('Card', on_delete=models.CASCADE)
#     card_list = models.ForeignKey('Card_list', on_delete=models.CASCADE)

class Card(models.Model):
    image = models.ImageField(upload_to='CardIco', blank=True, null=True, help_text="Выберите изображение для карточки")
    title = models.CharField(max_length=32, unique=True, blank=True, null=True)
    # list = models.ManyToManyField(Card_list, through='CardListRelationship')
    list_1 = models.CharField(max_length=32, blank=True, null=True)
    list_2 = models.CharField(max_length=32, blank=True, null=True)
    list_3 = models.CharField(max_length=32, blank=True, null=True)
    text = models.CharField(max_length=25, blank=True, null=True)
    cost = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f"карточка: {self.title}|{self.text}: {self.cost}"


class Example(models.Model):
    is_active_1 = models.BooleanField(default=True)
    number_1 = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)  # если нужно ограничить минимальное значение
        ]
    )
    image_1 = models.ImageField(upload_to='Examples', blank=True, null=True)
    title_1 = models.CharField(max_length=300, blank=True, null=True)
    text_1 = models.TextField(max_length=300, blank=True, null=True)

    is_active_2 = models.BooleanField(default=False)
    number_2 = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)  # если нужно ограничить минимальное значение
        ]
    )
    image_2 = models.ImageField(upload_to='Examples', blank=True, null=True)
    title_2 = models.CharField(max_length=300, blank=True, null=True)
    text_2 = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f" примеры: {self.number_1}.{self.title_1} | {self.number_2}.{self.title_2}"


class Offer(models.Model):
    image = models.ImageField(upload_to='Offer', blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    subtitle = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f" {self.title}, {self.subtitle}"

    def save(self, *args, **kwargs):
        if not self.pk and Offer.objects.exists():
            raise ValidationError("You can only create one instance of Settings.")
        return super(Offer, self).save(*args, **kwargs)


class Calendar(models.Model):
    calendar = models.ImageField(upload_to='Calendars', blank=True, null=True)


class Review(models.Model):
    review = models.ImageField(upload_to='Reviews', blank=True, null=True)


class Manual(models.Model):
    calendar = models.ImageField(upload_to='manual', blank=True, null=True)

    number_1 = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)  # если нужно ограничить минимальное значение
        ]
    )
    title_1 = models.CharField(max_length=50, blank=True, null=True)
    text_1 = models.CharField(max_length=200, blank=True, null=True)

    number_2 = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)  # если нужно ограничить минимальное значение
        ]
    )
    title_2 = models.CharField(max_length=50, blank=True, null=True)
    text_2 = models.CharField(max_length=200, blank=True, null=True)

    number_3 = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)  # если нужно ограничить минимальное значение
        ]
    )
    title_3 = models.CharField(max_length=50, blank=True, null=True)
    text_3 = models.CharField(max_length=200, blank=True, null=True)

    ico_1 = models.ImageField(upload_to='manual', blank=True, null=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    description_1 = models.CharField(max_length=500, blank=True, null=True)

    ico_2 = models.ImageField(upload_to='manual', blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)
    description_2 = models.CharField(max_length=500, blank=True, null=True)

    ico_3 = models.ImageField(upload_to='manual', blank=True, null=True)
    name_3 = models.CharField(max_length=50, blank=True, null=True)
    description_3 = models.CharField(max_length=500, blank=True, null=True)



    def save(self, *args, **kwargs):
        if not self.pk and Manual.objects.exists():
            raise ValidationError("You can only create one instance of Settings.")
        return super(Manual, self).save(*args, **kwargs)










