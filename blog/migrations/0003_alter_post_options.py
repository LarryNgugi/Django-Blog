# Generated by Django 3.2.6 on 2021-09-09 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post'},
        ),
    ]
