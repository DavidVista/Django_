from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Font(models.Model):
    TYPES = (
        ("Regular", "Regular"),
        ("Italic", "Italic"),
    )
    FAMILIES = (
        ('Vollkorn', 'Vollkorn'),
        ('Red Hat Mono', 'Red Hat Mono'),
        ('Open Sans', 'Open Sans')
    )
    family = models.CharField(max_length=63, choices=FAMILIES)
    weight = models.IntegerField(default=400, validators=[MaxValueValidator(900), MinValueValidator(400)])
    type = models.CharField(max_length=25, choices=TYPES)

class Text(models.Model):
    THEME = (
    ('Light', 'Light'),
    ('Dark', 'Dark'),
    ('Monokai', 'Monokai'),
    ('Chocolate', 'Chocolate')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255) # name varchar(255)
    text = models.TextField(null=True, blank=True)
    font_size = models.IntegerField(default=16, validators=[MaxValueValidator(98), MinValueValidator(12)])
    font = models.ManyToManyField(Font)
    theme = models.CharField(max_length=20, choices=THEME)
