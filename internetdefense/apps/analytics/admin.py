from django.contrib import admin
from analytics.models import Impression


class ImpressionAdmin(admin.ModelAdmin):
    list_filter = ('campaign', 'variant', 'is_autobroadcast', 'embedding_host')

admin.site.register(Impression, ImpressionAdmin)
