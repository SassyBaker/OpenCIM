from django.contrib import admin
from django.utils.html import format_html
from .models import Quantity


@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'on_hand',
        'on_order',
    )
    # fields = (
    #     'name',
    #     ('quantity', 'on_order'),
    #     'purchase_price',
    # )

    # readonly_fields = (
    #     'name',
    # )

    def on_hand(self, obj):
        if obj.quantity < 5:
            return format_html('<div style="color:red;">%s</div>' % obj.quantity)
        return obj.quantity

    on_hand.allow_tags = True
