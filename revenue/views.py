from django.shortcuts import render

from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.http import require_safe

from revenue.models import RevenueStatistic


@require_safe
def revenue_statistics(request):
    revenue_data = RevenueStatistic.objects.values("date", "name").annotate(
        total_revenue=Sum("revenue"),
        total_spend=Sum("spend__spend"),
        total_impressions=Sum("spend__impressions"),
        total_clicks=Sum("spend__clicks"),
        total_conversion=Sum("spend__conversion"),
    )

    return JsonResponse({"revenue_data": list(revenue_data)})
