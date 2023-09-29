from django.contrib import admin

from spend.models import SpendStatistic


class SpendAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "date",
        "spend",
        "impressions",
        "clicks",
        "conversion",
    )


admin.site.register(SpendStatistic, SpendAdmin)
