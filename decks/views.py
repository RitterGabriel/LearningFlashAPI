from rest_framework import views
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from setup.permission import IsDeckOwner
from .models import Deck, FlashCard
from .serializers import DeckSerializer, FlashCardSerializer
from datetime import datetime
from dateutil import parser
import pytz


def must_show_flashcard(flashcard):
    last_time_checked = parser.parse(str(flashcard.last_time_checked)).replace(tzinfo=pytz.utc)
    datetime_variation = datetime.now(pytz.utc) - last_time_checked
    return flashcard.domain_level ** 2 <= datetime_variation.days


class DeckViewSet(views.APIView):
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    def get(self, request, id):
        deck = Deck.objects.get(id=id)
        self.check_object_permissions(request, deck)
        serializer = DeckSerializer(deck)
        return Response(serializer.data, status=200)
    

class DecksViewSet(views.APIView):
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
    

class FlashCardsViewSet(views.APIView):
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    
    def get(self, request, id):
        deck = Deck.objects.get(id=id)
        self.check_object_permissions(request, deck)
        flashcards = filter(must_show_flashcard, FlashCard.objects.filter(deck=deck))
        serializer = FlashCardSerializer(flashcards, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, id):
        data = request.data
        data['deck'] = id
        deck = Deck.objects.get(id=id)
        self.check_object_permissions(request, deck)
        serializer = FlashCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FlashCardViewSet(views.APIView):
    permission_classes = [IsDeckOwner, permissions.IsAuthenticated]
    
    def put(self, request, id):
        flash_card = FlashCard.objects.get(id=id)
        serializer = FlashCardSerializer(flash_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        flash_card = FlashCard.objects.filter(id=id) 
        flash_card.delete()
        return Response(data={'status': 'deletado com sucesso'}, status=201)
