# Generated by Django 3.0.7 on 2020-06-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_applay'),
    ]

    operations = [
        migrations.AddField(
            model_name='applay',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
