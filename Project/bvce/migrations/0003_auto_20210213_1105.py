# Generated by Django 3.1 on 2021-02-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvce', '0002_auto_20210213_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]