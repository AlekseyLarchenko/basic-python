from django.urls import path
from .views import (
    IndexView,
    StadiumListView,
    TeamListView,
    NewsListView,
    TeamDetailView,
    NewsDetailView,
    StadiumDetailView,
)

app_name = "premier_league"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('stadiums/', StadiumListView.as_view(), name='stadium_list'),
    path('stadiums/<int:pk>/', StadiumDetailView.as_view(), name='stadium_detail'),
    path('clubs/', TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
