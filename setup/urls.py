from django.urls import path
from django.contrib import admin
from users.views import UserView, LoginView
from decks.views import (
    DecksView, 
    DeckView, 
    FlashCardsView, 
    FlashCardView
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
    path('api/users/', UserView.as_view(),),
    path('api/login/', LoginView.as_view()),
    path('api/decks/', DecksView.as_view()),
    path('api/decks/<int:id>/', DeckView.as_view()),
    path('api/decks/<int:id>/flashcards/', FlashCardsView.as_view()),
    path('api/flashcards/<int:id_>/', FlashCardView.as_view()),
    path('api/summaries/', SummariesView.as_view()),
    path('api/summaries/<int:id>/', SummaryView.as_view()),
    path('api/summary_genders/', SummaryGenderView.as_view()),
    path('api/authors/', AuthorsView.as_view()),
    path('api/audio/<str:phrase>', AudioView.as_view()),
    path('api/phrases/<str:phrase>', PhraseView.as_view()),
]
