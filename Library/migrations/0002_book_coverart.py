# Generated by Django 4.1.5 on 2023-05-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='coverart',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
