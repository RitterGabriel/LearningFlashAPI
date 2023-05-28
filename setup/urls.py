from django.urls import path
from django.contrib import admin
from decks.views import DecksViewSet, DeckViewSet, FlashCardsViewSet, FlashCardViewSet
from users.views import UserViewSet
from summaries.views import SummaryViewSet, SummariesViewSet, SummaryGenderViewSet, AudioViewSet, AuthorViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserViewSet.as_view(),),
    path('api/decks/', DecksViewSet.as_view()),
    path('api/decks/<int:id>/', DeckViewSet.as_view()),
    path('api/decks/<int:id>/flashcards/', FlashCardsViewSet.as_view()),
    path('api/flashcards/<int:id>/', FlashCardViewSet.as_view()),
    path('api/summaries/', SummariesViewSet.as_view()),
    path('api/summaries/<int:id>/', SummaryViewSet.as_view()),
    path('api/summary_genders/', SummaryGenderViewSet.as_view()),
    path('api/authors/', AuthorViewSet.as_view()),
    path('api/audio/<str:phrase>', AudioViewSet.as_view()),
]
