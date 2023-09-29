from django.contrib import admin

from revenue.models import RevenueStatistic


class RevenueAdmin(admin.ModelAdmin):
    list_display = ("id", "spend", "date", "revenue")


admin.site.register(RevenueStatistic, RevenueAdmin)
