from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Font(models.Model):
    TYPES = (
        ("reg", "Regular"),
        ("ital", "Italic"),
    )
    FAMILIES = (
        ('Vollkorn', 'Vollkorn'),
        ('Red Hat Mono', 'Red Hat Mono'),
        ('Open Sans', 'Open Sans')
    )
    family = models.CharField(max_length=63, choices=FAMILIES)
    weight = models.IntegerField(default=400, validators=[MaxValueValidator(600), MinValueValidator(400)])
    type = models.CharField(max_length=25, choices=TYPES)


class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)  # name varchar(255)
    text = models.TextField(null=True, blank=True)
    date_of_creation = models.DateField(null=True)
    date_of_recent_change = models.DateField(null=True)
    font_size = models.IntegerField(default=16, validators=[MaxValueValidator(98), MinValueValidator(12)])
    font = models.ForeignKey(Font, on_delete=models.CASCADE, null=True)
    THEME = (
        ('while black', 'Light'),
        ('black white', 'Dark'),
        ('black red', 'Monokai')
    )
    theme_type = models.CharField(max_length=25, choices=THEME, null=True)
