# Generated by Django 3.2.8 on 2021-11-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_coursera_coursera_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursera',
            name='be_pr',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
