# Generated by Django 4.1.5 on 2023-01-18 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_idea_dev_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='dev_tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.devtool'),
        ),
    ]
