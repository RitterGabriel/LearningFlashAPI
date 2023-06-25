from django.urls import path
from django.contrib import admin
from users.views import UserViewSet, LoginViewSet
from decks.views import (
    DecksViewSet, 
    DeckViewSet, 
    FlashCardsViewSet, 
    FlashCardViewSet
)
from summaries.views import (
    SummaryView,
    SummariesView, 
    SummaryGenderView, 
    AudioView, 
    AuthorsView, 
    PhraseView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserViewSet.as_view(),),
    path('api/login/', LoginViewSet.as_view()),
    path('api/decks/', DecksViewSet.as_view()),
    path('api/decks/<int:id>/', DeckViewSet.as_view()),
    path('api/decks/<int:id>/flashcards/', FlashCardsViewSet.as_view()),
    path('api/flashcards/<int:id>/', FlashCardViewSet.as_view()),
    path('api/summaries/', SummariesView.as_view()),
    path('api/summaries/<int:id>/', SummaryView.as_view()),
    path('api/summary_genders/', SummaryGenderView.as_view()),
    path('api/authors/', AuthorsView.as_view()),
    path('api/audio/<str:phrase>', AudioView.as_view()),
    path('api/phrases/<str:phrase>', PhraseView.as_view())
]
