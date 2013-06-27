from django.contrib import admin
from campaigns.models import Campaign, Variant


class CampaignAdmin(admin.ModelAdmin):
    """
    Simple admin for the Campaign model
    """
    prepopulated_fields = {'slug': ('name',)}


class VariantAdmin(admin.ModelAdmin):
    """
    Simple admin for the Variant model
    """
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Variant, VariantAdmin)
