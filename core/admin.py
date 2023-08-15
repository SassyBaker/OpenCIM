from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Cable, Type, Color, Length, Connector, Brand


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )


admin.site.register(Cable)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Length)
admin.site.register(Connector)
admin.site.register(Brand)
