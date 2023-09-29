from django.urls import path

from revenue.views import revenue_statistics

app_name = "revenue"

urlpatterns = [
    path("revenue-statistics/", revenue_statistics, name="revenue-statistics"),
]
