from django.urls import path

from spend.views import spend_statistics

app_name = "spend"

urlpatterns = [
    path("spend-statistics/", spend_statistics, name="spend-statistics"),
]
