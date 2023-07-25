from django.views.generic import ListView, DetailView, TemplateView
from .models import Stadium, Team, News


class StadiumListView(ListView):
    model = Stadium
    template_name = 'premier_league:stadium_list.html'
    context_object_name = 'stadiums'


class StadiumDetailView(DetailView):
    model = Stadium
    template_name = 'premier_league:stadium_detail.html'
    context_object_name = 'stadium'


class TeamListView(ListView):
    model = Team
    template_name = 'premier_league:team_list.html'
    context_object_name = 'teams'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'premier_league:team_detail.html'
    context_object_name = 'team'


class NewsListView(ListView):
    model = News
    template_name = 'premier_league:news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = 'premier_league:news_detail.html'
    context_object_name = 'news'


class PlIndexView(TemplateView):
    template_name = "premier_league/index.html"
