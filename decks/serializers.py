from rest_framework import serializers
from .models import Deck, FlashCard


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'name', 'description', 'user']


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['id', 'phrase', 'translated_phrase', 'last_time_checked', 'domain_level', 'deck']
    
