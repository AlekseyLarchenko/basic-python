from django.urls import path
from .views import pl_index

app_name = "pl"

urlpatterns = [
    path("", pl_index, name="index")
]

