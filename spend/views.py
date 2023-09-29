from django.shortcuts import render

from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.http import require_safe

from .models import SpendStatistic


@require_safe
def spend_statistics(request):
    spend_data = SpendStatistic.objects.values("date", "name").annotate(
        total_spend=Sum("spend"),
        total_impressions=Sum("impressions"),
        total_clicks=Sum("clicks"),
        total_conversion=Sum("conversion"),
        total_revenue=Sum("revenuestatistic__revenue"),
    )

    return JsonResponse({"spend_data": list(spend_data)})
