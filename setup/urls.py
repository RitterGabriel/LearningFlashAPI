from django.urls import path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from decks.views import DecksViewSet, DeckViewSet, FlashCardsViewSet, FlashCardViewSet
from users.views import UserViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserViewSet.as_view()),
    path('api/decks/', DecksViewSet.as_view()),
    path('api/decks/<int:id>/', DeckViewSet.as_view()),
    path('api/decks/<int:id>/flashcards/', FlashCardsViewSet.as_view()),
    path('api/flashcards/<int:id>/', FlashCardViewSet.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
