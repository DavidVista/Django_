# Generated by Django 4.0.3 on 2022-04-01 07:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_type', models.CharField(choices=[('while black', 'Light'), ('black white', 'Dark'), ('black red', 'Monokai')], max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='text',
            name='date_of_creation',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='text',
            name='date_of_recent_change',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='font',
            name='type',
            field=models.CharField(choices=[('reg', 'Regular'), ('ital', 'Italic')], max_length=25),
        ),
        migrations.AlterField(
            model_name='font',
            name='weight',
            field=models.IntegerField(default=400, validators=[django.core.validators.MaxValueValidator(600), django.core.validators.MinValueValidator(400)]),
        ),
        migrations.RemoveField(
            model_name='text',
            name='font',
        ),
        migrations.AddField(
            model_name='text',
            name='font',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reapp.font'),
        ),
        migrations.AlterField(
            model_name='text',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reapp.theme'),
        ),
    ]