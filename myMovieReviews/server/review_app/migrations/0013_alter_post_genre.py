# Generated by Django 4.1.5 on 2023-01-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0012_alter_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(blank=True, choices=[('액션', '액션'), ('SF', 'SF'), ('로맨스', '로맨스'), ('코미디', '코미디'), ('느와르', '느와르'), ('공포', '공포'), ('스릴러', '스릴러')], max_length=10),
        ),
    ]