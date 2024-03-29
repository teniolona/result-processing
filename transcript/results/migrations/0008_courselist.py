# Generated by Django 4.2.2 on 2024-02-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_delete_courselist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursecode', models.CharField(max_length=16, verbose_name='Course Code')),
                ('coursetitle', models.CharField(max_length=64, verbose_name='Course Title')),
                ('coursecredit', models.IntegerField()),
                ('coursemark', models.IntegerField()),
                ('lettergrade', models.CharField(max_length=16, verbose_name='Letter Grade')),
                ('gp', models.IntegerField()),
                ('weightedgp', models.IntegerField()),
            ],
        ),
    ]
