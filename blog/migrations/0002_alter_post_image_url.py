# Generated by Django 3.2.6 on 2021-09-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
