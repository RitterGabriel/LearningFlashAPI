from django.urls import path
from .views import DeckView, DecksView, FlashCardView, FlashCardsView


urlpatterns = [
    path('decks/', DecksView.as_view(), name='decks'),
    path('decks/<int:id>/', DeckView.as_view(), name='deck'),
    path('decks/<int:id>/flashcards/', FlashCardsView.as_view(), name='flashcard'),
    path('flashcards/<int:id_>/', FlashCardView.as_view(), name='flashcards'),
]
