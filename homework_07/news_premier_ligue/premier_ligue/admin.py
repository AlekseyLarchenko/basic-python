from django.contrib import admin

# Register your models here.
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = "id", "name", "shortname", "stadium", "website", "league"
    list_display_links = "id", "name", "shortname"
