from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from setup.permission import IsDeckOwner
from .models import Deck, FlashCard
from .serializers import DeckSerializer, FlashCardSerializer
from datetime import datetime
from dateutil import parser
import pytz


class DeckView(views.APIView):
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    
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
    permission_classes = [permissions.IsAuthenticated]
    
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
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    
    @staticmethod
    def must_show_flashcard(flashcard):
        last_time_checked = parser.parse(str(flashcard.last_time_checked)).replace(tzinfo=pytz.utc)
        datetime_variation = datetime.now(pytz.utc) - last_time_checked
        if flashcard.domain_level ** 2 <= datetime_variation.days:
            print(datetime_variation.days)
        return flashcard.domain_level ** 2 <= datetime_variation.days

    def get(self, request, id):
        decks = Deck.objects.filter(id=id)
        if len(decks) > 0:
            deck = decks[0]
            self.check_object_permissions(request, deck)
            if request.GET.get('get_all') == 'false':
                flashcards = [flashcard for flashcard in FlashCard.objects.filter(deck=deck) if self.must_show_flashcard(flashcard)]
            else:
                flashcards = FlashCard.objects.filter(deck=deck)
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


class FlashCardView(views.APIView):
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    
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
        return Response(data={'status': 'deletado com sucesso'}, status=204)
