# Generated by Django 4.1.5 on 2023-01-24 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_comment',
            new_name='postcomment',
        ),
    ]
