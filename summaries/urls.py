from django.urls import path
from .views import SummaryView, SummariesView, SummaryGenderView, PhraseView, FavoritesView, AuthorsView


urlpatterns = [
    path('summaries/', SummariesView.as_view()),
    path('summaries/<int:id>/', SummaryView.as_view()),
    path('summary_genders/', SummaryGenderView.as_view()),
    path('authors/', AuthorsView.as_view()),
    path('phrases/<str:phrase>', PhraseView.as_view()),
    path('favorites/', FavoritesView.as_view()),
]
