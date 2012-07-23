from django.contrib import admin
from campaigns.models import Campaign, HTMLOverride, Variant


class HTMLOverrideInline(admin.TabularInline):
    max_num = len(Variant.objects.all())
    model = HTMLOverride


class CampaignAdmin(admin.ModelAdmin):
    inlines = [
        HTMLOverrideInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


class VariantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Variant, VariantAdmin)
