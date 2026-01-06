from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'date_of_birth',
        'role',
        'is_staff',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')
    ordering = ('id',)
    fields = (
        'email',
        'password',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'date_of_birth',
        'role',
        'is_staff',
        'is_active',
    )
