# Generated by Django 2.1 on 2019-05-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField()),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='likes_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='likes',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='likes',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]