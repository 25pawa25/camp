from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'form', )
    fieldsets = (
        ('Пользователь', {
            'fields': ('fio',
                       'phone',
                       'form',
                       ),
        }),

    )

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('phone', )
    fieldsets = (
        ('Телефон', {
            'fields': ('phone',
                       ),
        }),

    )
