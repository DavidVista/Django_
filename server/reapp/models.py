from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Text(models.Model):
    THEME = (
        ('while black', 'Light'),
        ('black white', 'Dark'),
        ('black red', 'Monokai'),
        ('brown yellow', 'Chocolate')
    )
    TYPES = (
        ("reg", "Regular"),
        ("italic", "Italic"),
        ("bold", "Bold"),
        ('bold italic', "Bold & Italic")
    )
    FAMILIES = (
        ('Vollkorn', 'Vollkorn'),
        ('Red Hat Mono', 'Red Hat Mono'),
        ('Open Sans', 'Open Sans'),
        ('Roboto Slab', 'Roboto Slab')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)  # name varchar(255)
    text = models.TextField(null=True, blank=True)
    # date_of_creation = models.DateField(null=True)
    # date_of_recent_change = models.DateField(null=True)
    font_size = models.IntegerField(default=16, validators=[MaxValueValidator(98), MinValueValidator(12)])
    font_family = models.CharField(max_length=63, choices=FAMILIES, null=True)
    font_type = models.CharField(max_length=25, choices=TYPES, null=True)
    theme_type = models.CharField(max_length=25, choices=THEME, null=True)
