from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    img = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'


class Genre(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    poster = models.ImageField(upload_to='movies/')
    year = models.IntegerField('Year', default=0)
    country = models.CharField('Country', max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='Directors', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actors', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    world_premiere = models.DateField('World Premiere', default=date.today)
    budget = models.IntegerField('Budget', default=0)
    fees_in_usa = models.IntegerField('Fees in the USA', default=0, help_text='$')
    fees_in_world = models.IntegerField('Fees in the world', default=0, help_text='$')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    img = models.SlugField(max_length=200, unique=True)
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie short'
        verbose_name_plural = 'Movie shorts'


class RatingStar(models.Model):
    value = models.IntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating star'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP', max_length=20)
    star = models.ForeignKey(RatingStar, verbose_name='Star', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'

class Review(models.Model):
    email = models.EmailField('Email', max_length=100)
    name = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True, related_name='children') #то поле, на которое мы завязываемся, указываем к какому отзыву мы привязываемся
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'

