# Generated by Django 3.2.8 on 2021-11-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_classroom_class_the_sorting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='c_name',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]
