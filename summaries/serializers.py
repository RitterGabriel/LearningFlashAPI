from rest_framework import serializers
from .models import Author, Summary, SummaryGender, Favorite


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class CreateSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = 'title', 'author', 'gender', 'text_content', 'translated_text'


class SummariesSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.author_name', read_only=True)
    gender = serializers.CharField(source='gender.gender_name', read_only=True)

    class Meta:
        model = Summary
        fields = 'id', 'title', 'author', 'gender', 'image'


class SummarySerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.author_name', read_only=True)
    gender = serializers.CharField(source='gender.gender_name', read_only=True)

    class Meta:
        model = Summary
        fields = '__all__'


class SummaryGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryGender
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
