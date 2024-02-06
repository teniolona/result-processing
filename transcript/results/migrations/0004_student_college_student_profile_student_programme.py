# Generated by Django 4.2.2 on 2024-01-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_student_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(null=True, upload_to='student/'),
        ),
        migrations.AddField(
            model_name='student',
            name='programme',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
