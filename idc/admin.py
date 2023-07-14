from django.contrib import admin
from django.utils.html import format_html
from .models import CableInventory, CableInventoryEditHistory


# Register your models here.
@admin.register(CableInventory)
class CableInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'cable',
        'on_hand',
        'on_order',
    )

    # readonly_fields = (
    #     'cable',
    # )

    def on_hand(self, obj):
        if obj.quantity < 5:
            return format_html('<div style="color:red;">%s</div>' % obj.quantity)
        return obj.quantity

    on_hand.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.save(request=request)


@admin.register(CableInventoryEditHistory)
class EditHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'datetime',
        'parent',
        'edited_by',
    )

    # Make all fields read only
    readonly_fields = tuple([f.name for f in CableInventoryEditHistory._meta.fields])
