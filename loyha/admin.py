from django.contrib import admin
from .models import Loyha

@admin.register(Loyha)
class LoyhaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
