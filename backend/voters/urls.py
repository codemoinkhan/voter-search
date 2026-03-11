from django.urls import path
from .views import search_voter, search_page

urlpatterns = [
    path("search/", search_voter),
    path("app/", search_page),
]