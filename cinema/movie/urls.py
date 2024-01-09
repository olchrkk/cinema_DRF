from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .views import MovieListView, MovieDetailView, ReviewCreateView, AddStarRatingView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/', ReviewCreateView.as_view(), name='review_create'),
    path('rating/', AddStarRatingView.as_view(), name='add_star_rating')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)