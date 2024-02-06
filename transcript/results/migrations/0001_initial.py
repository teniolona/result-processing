# Generated by Django 4.2.2 on 2024-01-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matricno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last Name')),
                ('level', models.IntegerField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]