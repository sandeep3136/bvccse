# Generated by Django 3.1.3 on 2021-02-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvce', '0006_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
