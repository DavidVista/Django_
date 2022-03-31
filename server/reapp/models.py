from django.db import models

class Text(models.Model):
    THEME = (
    ('Light', 'Light'),
    ('Dark', 'Dark'),
    ('Monokai', 'Monokai'),
    ('Chocolate', 'Chocolate')
    )

    name = models.CharField(max_length=255) # name varchar(255)
    text = models.TextField(null=True, blank=False)
    font_size = models.IntegerField()
    theme = models.CharField(max_length=20, blank=False, choices=THEME)

