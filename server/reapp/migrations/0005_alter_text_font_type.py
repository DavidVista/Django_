# Generated by Django 4.0.3 on 2022-04-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reapp', '0004_remove_text_font_text_font_family_text_font_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='font_type',
            field=models.CharField(choices=[('reg', 'Regular'), ('italic', 'Italic'), ('bold', 'Bold')], max_length=25, null=True),
        ),
    ]