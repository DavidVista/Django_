# Generated by Django 4.0.3 on 2022-04-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reapp', '0002_theme_text_date_of_creation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='theme',
        ),
        migrations.AddField(
            model_name='text',
            name='theme_type',
            field=models.CharField(choices=[('while black', 'Light'), ('black white', 'Dark'), ('black red', 'Monokai')], max_length=25, null=True),
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]