from django.contrib import admin
from .models import Cable, EditHistory, Brand, Type, Color, Connector, Length


# Register your models here.
@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
    )

    readonly_fields = (
        'name',
    )

    def save_model(self, request, obj, form, change):
        obj.save(request=request)


@admin.register(EditHistory)
class EditHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'datetime',
        'parent',
        'edited_by',
    )

    # Make all fields read only
    readonly_fields = tuple([f.name for f in EditHistory._meta.fields])


admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Connector)
admin.site.register(Length)
admin.site.register(Type)
