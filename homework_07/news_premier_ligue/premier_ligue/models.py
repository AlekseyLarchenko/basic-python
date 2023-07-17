from django.db import models


# Create your models here.
class Stadium(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    capacity = models.IntegerField(null=False)
    brokeground = models.DateField()
    architect = models.CharField(max_length=20)
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    nicknames = models.CharField(max_length=50, null=True)
    shortname = models.CharField(max_length=50, null=True)
    founded = models.DateField()
    stadium = models.OneToOneField(Stadium, on_delete=models.SET_NULL, null=True, blank=True, related_name='team')
    website = models.CharField(max_length=50)
    league = models.CharField(max_length=20)
    description = models.TextField()
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return f"Team <{self.pk}, {self.name!r}, {self.stadium!r}>"


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shortname = models.CharField(max_length=50, null=True)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='news')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='news')
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.shortname


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teams = models.ManyToManyField(Team, related_name='users')
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return f"{self.created_at} - {self.author} - {self.content}"
