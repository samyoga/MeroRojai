# Generated by Django 2.0.5 on 2018-10-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
                ('book_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('book_cover', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casts', models.CharField(max_length=500)),
                ('movie_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('movie_poster', models.CharField(max_length=1000)),
            ],
        ),
    ]
