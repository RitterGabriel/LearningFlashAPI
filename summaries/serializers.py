from rest_framework import serializers
from .models import Author, Audio, Summary, SummaryGender


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['audio_name', 'audio_content']


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class SummaryGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryGender
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}