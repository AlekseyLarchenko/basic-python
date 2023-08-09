from django.test import TestCase
from django.urls import reverse
from .models import Stadium, Team, News, Author, User


class PremierLeagueTests(TestCase):

    def setUp(self):
        self.stadium = Stadium.objects.create(
            name='Stadium 1',
            location='Location 1',
            capacity=10000,
            brokeground='2023-01-01',
            architect='Architect 1',
            phone='1234567890',
            guid='11111111-1111-1111-1111-111111111111'
        )

        self.team = Team.objects.create(
            name='Team 1',
            nicknames='Nickname 1',
            shortname='Shortname 1',
            founded='2020-01-01',
            stadium=self.stadium,
            website='https://www.example.com',
            league='League 1',
            description='Description 1',
            guid='22222222-2222-2222-2222-222222222222'
        )

        self.author = Author.objects.create(
            name='Author 1',
            email='author@example.com',
            guid='33333333-3333-3333-3333-333333333333'
        )

        self.news = News.objects.create(
            shortname='News 1',
            description='News description 1',
            team=self.team,
            author=self.author,
            guid='44444444-4444-4444-4444-444444444444'
        )

        self.user = User.objects.create(
            name='User 1',
            email='user@example.com',
            guid='55555555-5555-5555-5555-555555555555'
        )
        self.user.teams.add(self.team)

    def tearDown(self):
        Stadium.objects.all().delete()
        Team.objects.all().delete()
        Author.objects.all().delete()
        News.objects.all().delete()
        User.objects.all().delete()

    def test_stadium_list_view(self):
        response = self.client.get(reverse('premier_league:stadium_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/stadium_list.html')
        self.assertContains(response, self.stadium.name)

    def test_stadium_detail_view(self):
        response = self.client.get(reverse('premier_league:stadium_detail', kwargs={'pk': self.stadium.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/stadium_detail.html')
        self.assertEqual(response.context['stadium'], self.stadium)

    def test_team_list_view(self):
        response = self.client.get(reverse('premier_league:team_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/team_list.html')
        self.assertContains(response, self.team.shortname)

    def test_team_detail_view(self):
        response = self.client.get(reverse('premier_league:team_detail', kwargs={'pk': self.team.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/team_detail.html')
        self.assertEqual(response.context['team'], self.team)

    def test_news_list_view(self):
        response = self.client.get(reverse('premier_league:news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/news_list.html')
        self.assertContains(response, self.news.shortname)

    def test_news_detail_view(self):
        response = self.client.get(reverse('premier_league:news_detail', kwargs={'pk': self.news.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/news_detail.html')
        self.assertEqual(response.context['news'], self.news)

    def test_index_view(self):
        response = self.client.get(reverse('premier_league:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premier_league/index.html')

    def test_user_teams(self):
        teams = self.user.teams.all()
        self.assertEqual(teams.count(), 1)
        self.assertEqual(teams[0], self.team)
