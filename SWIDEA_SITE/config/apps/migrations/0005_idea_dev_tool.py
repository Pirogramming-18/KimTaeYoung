# Generated by Django 4.1.5 on 2023-01-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_idea_dev_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='dev_tool',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
