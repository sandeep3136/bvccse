# Generated by Django 3.1 on 2021-02-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvce', '0004_auto_20210213_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]