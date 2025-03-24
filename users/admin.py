from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'phone_number', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('id', 'name', 'username', 'phone_number',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at',)
    fieldsets = (
        ('Personal Info', {'fields': ('id', 'username', 'name', 'phone_number',)}),
        ('Date Info', {'fields': ('created_at', 'updated_at')}),
        ('Permissions and others', {'fields': ('is_staff', 'is_superuser',)}),
    )
