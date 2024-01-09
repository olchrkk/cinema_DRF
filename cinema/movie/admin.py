from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Actor, Movie, Genre, MovieShots, RatingStar, Rating, Review


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_img')
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height="100">')
    get_img.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    list_display_links = ('name', )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    save_on_top = True
    save_as = True
    list_editable = ('draft', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'img','movie')
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height="100">')

    get_img.short_description = 'Image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip','star','movie')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'text', 'parent','movie', 'id')
    readonly_fields = ('name', 'email')

admin.site.register(RatingStar)

admin.site.site_title = 'Cinema'
admin.site.site_header = 'Cinema'
