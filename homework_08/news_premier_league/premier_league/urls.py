from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stadiums/', views.StadiumListView.as_view(), name='stadium_list'),
    path('stadiums/<int:pk>/', views.StadiumDetailView.as_view(), name='stadium_detail'),
    path('clubs/', views.TeamListView.as_view(), name='team_list'),
    path('clubs/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]
