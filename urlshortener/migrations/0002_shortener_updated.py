# Generated by Django 4.2.4 on 2023-08-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortener',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
