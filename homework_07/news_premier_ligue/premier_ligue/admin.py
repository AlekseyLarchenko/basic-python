from django.contrib import admin

# Register your models here.
from .models import Stadium, Team, Author, News, User, Comments


@admin.register(Stadium)
class TeamAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Stadium"
        verbose_name_plural = "Stadium"

    list_display = "id", "name", "location", "capacity", "brokeground"
    list_display_links = "id", "name"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = "id", "name", "shortname", "stadium", "website", "league"
    list_display_links = "id", "name", "shortname"


@admin.register(Author)
class TeamAdmin(admin.ModelAdmin):
    list_display = "id", "name", "email"
    list_display_links = "id", "name"


@admin.register(News)
class TeamAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    list_display = "id", "created_at", "shortname", "author"
    list_display_links = "id", "shortname"


@admin.register(User)
class TeamAdmin(admin.ModelAdmin):
    list_display = "id", "name", "email"
    list_display_links = "id", "name"


@admin.register(Comments)
class TeamAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Comments"

    list_display = "id", "created_at", "news", "author"
    list_display_links = "id", "news"
