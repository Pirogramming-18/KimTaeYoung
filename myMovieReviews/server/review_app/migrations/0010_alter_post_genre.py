# Generated by Django 4.1.5 on 2023-01-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0009_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(max_length=10),
        ),
    ]
