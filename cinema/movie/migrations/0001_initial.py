# Generated by Django 5.0.1 on 2024-01-07 17:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Actors and directors',
                'verbose_name_plural': 'Actors and directors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Rating star',
                'verbose_name_plural': 'Rating star',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='movies/')),
                ('year', models.IntegerField(default=0, verbose_name='Year')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='World Premiere')),
                ('budget', models.IntegerField(default=0, verbose_name='Budget')),
                ('fees_in_usa', models.IntegerField(default=0, help_text='$', verbose_name='Fees in the USA')),
                ('fees_in_world', models.IntegerField(default=0, help_text='$', verbose_name='Fees in the world')),
                ('url', models.SlugField(max_length=200, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movie.actor', verbose_name='Actors')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movie.actor', verbose_name='Directors')),
                ('genres', models.ManyToManyField(to='movie.genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.SlugField(max_length=200, unique=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Movie')),
            ],
            options={
                'verbose_name': 'Movie short',
                'verbose_name_plural': 'Movie shorts',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='IP')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ratingstar', verbose_name='Star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Text')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.review', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Review',
            },
        ),
    ]