# Generated by Django 4.1.5 on 2023-01-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0013_alter_post_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
