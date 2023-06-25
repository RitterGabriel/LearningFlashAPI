from rest_framework import serializers
from .models import Author, Audio, Summary, SummaryGender, Phrase


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['audio_name', 'audio_content']


class CreateSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = 'title', 'author', 'gender', 'text_content', 'translated_text'


class SummariesSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.author_name', read_only=True)
    gender = serializers.CharField(source='gender.gender_name', read_only=True)
    class Meta:
        model = Summary
        fields = 'id', 'title', 'author', 'gender',


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


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = '__all__'