from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from setup.permission import IsDeckOwner
from .models import Deck, FlashCard
from .serializers import DeckSerializer, FlashCardSerializer
from datetime import datetime, date
from dateutil import parser
import pytz


class DeckView(views.APIView):
    permission_classes = IsDeckOwner, IsAuthenticated
    
    def get(self, request, id):
        deck = Deck.objects.get(id=id)
        self.check_object_permissions(request, deck)
        serializer = DeckSerializer(deck)
        return Response(serializer.data, status=200)
    
    def delete(self, request, id):
        deck = Deck.objects.filter(id=id)
        deck.delete()
        return Response(data={'status': 'deletado com sucesso'}, status=204)


class DecksView(views.APIView):
    permission_classes = IsAuthenticated,
    
    def get(self, request):
        decks = Deck.objects.filter(user=request.user)
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = DeckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class FlashCardsView(views.APIView):
    permission_classes = IsDeckOwner, IsAuthenticated

    def get(self, request, id):
        decks = Deck.objects.filter(id=id)
        if decks:
            deck, = decks
            self.check_object_permissions(request, deck)
            if request.GET.get('get_all') == 'false':
                flashcards = self._filter_flashcards_that_must_be_showed(FlashCard.objects.filter(deck=deck))
            else:
                flashcards = [self._add_days_to_appear_to_flashcard(flashcard)
                              for flashcard in FlashCard.objects.filter(deck=deck)]
            serializer = FlashCardSerializer(flashcards, many=True)
            return Response(serializer.data, status=200)
        return Response({'status': '404'}, status=404)

    def post(self, request, id):
        data = request.data
        data['deck'] = id
        decks = Deck.objects.filter(id=id)
        if len(decks) > 0:
            deck = decks[0]
            self.check_object_permissions(request, deck)
            serializer = FlashCardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'status': '404'}, status=404)

    def _get_days_to_appear_amount(self, flashcard):
        last_time_checked_date = flashcard.last_time_checked.date()
        passed_days = (date.today() - last_time_checked_date).days
        days_to_appear = 2 ** flashcard.domain_level - passed_days if flashcard.domain_level > 0 else 0
        return days_to_appear if days_to_appear > 0 else 0

    def _add_days_to_appear_to_flashcard(self, flashcard):
        days_to_appear = self._get_days_to_appear_amount(flashcard)
        flashcard.days_to_appear = days_to_appear
        return flashcard

    def _filter_flashcards_that_must_be_showed(self, flashcards):
        filtered_flashcards = []
        for flashcard in flashcards:
            flashcard = self._add_days_to_appear_to_flashcard(flashcard)
            if flashcard.days_to_appear == 0:
                filtered_flashcards.append(flashcard)
        return filtered_flashcards




class FlashCardView(views.APIView):
    permission_classes = IsDeckOwner, IsAuthenticated
    
    def put(self, request, id_):
        has_good_domain_level = request.data.get('has_good_domain_level')
        if has_good_domain_level is None:
            return Response({'has_good_domain_level': 'campo obrigatório'}, status=400)
        flash_card = FlashCard.objects.get(id=id_)
        data = {
            'id': flash_card.id, 
            'phrase': flash_card.phrase, 
            'translated_phrase': flash_card.translated_phrase, 
            'last_time_checked': flash_card.last_time_checked,
            'domain_level': flash_card.domain_level + 1 if has_good_domain_level else 0,
            'deck': flash_card.deck.id,
        }
        serializer = FlashCardSerializer(flash_card, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id_):
        flash_card = FlashCard.objects.filter(id=id_) 
        flash_card.delete()
        return Response({'status': 'deletado com sucesso'}, status=200)
