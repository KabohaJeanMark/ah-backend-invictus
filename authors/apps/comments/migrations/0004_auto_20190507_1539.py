# Generated by Django 2.1 on 2019-05-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_likes_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='liked',
        ),
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
