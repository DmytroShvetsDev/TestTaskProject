from django.db import models
from django.shortcuts import render

from django.db.models import Sum, Subquery, OuterRef
from django.http import JsonResponse
from django.views.decorators.http import require_safe

from revenue.models import RevenueStatistic
from .models import SpendStatistic


@require_safe
def spend_statistics(request):
    subquery = RevenueStatistic.objects.filter(spend=OuterRef('pk')).values('spend').annotate(
        total_revenue=Sum('revenue')
    ).values('total_revenue')[:1]

    spend_data = SpendStatistic.objects.annotate(
        total_revenue=Subquery(subquery, output_field=models.DecimalField(max_digits=9, decimal_places=2))
    ).values("date", "name").annotate(
        total_spend=Sum("spend"),
        total_impressions=Sum("impressions"),
        total_clicks=Sum("clicks"),
        total_conversion=Sum("conversion"),
    )

    return JsonResponse({"spend_data": list(spend_data)})
