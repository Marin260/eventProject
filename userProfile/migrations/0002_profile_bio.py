# Generated by Django 4.0.2 on 2022-02-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='', max_length=150),
        ),
    ]
