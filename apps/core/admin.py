from django.contrib import admin
from .models import News


class AdminNews(admin.ModelAdmin):
    search_fields = ('site',)

admin.site.register(News, AdminNews)
