from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Team

def pl_index(request: HttpRequest) -> HttpResponse:
    teams = Team.objects.order_by("id").all()
    return render(
        request=request,
        template_name="premier_league/index.html",
        context={
            "teams": teams,
        },
    )
