# Generated by Django 4.2.2 on 2024-01-13 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
    ]
