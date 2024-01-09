from rest_framework import serializers
from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Review


class FilterReviewListSerializers(serializers.ListSerializers):
    def to_representation(self, obj):
        data = obj.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, obj):
        serializers = self.parent.parent.__class__(obj, context=self.context)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'category')


class ReviewCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewListSerializers
        model = Review
        fields = ('name', 'text', 'children')


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True) #вывод названия поля name->'Category' in admin pannel
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True) #тоже самое, но для многих
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializers(many=True) #в классе Movie>movie related_name=reviews

    class Meta:
        model = Movie
        exclude = ('draft', )


class CreateRatingSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip'),
            movie=validated_data.get('movie'),
            defaults={'star': validated_data.get('star')}
        )
        return rating


    class Meta:
        model = Rating
        fields = ('star','movie')
