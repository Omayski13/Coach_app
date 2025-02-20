from django.contrib import admin

from coach_app.listings.models import Listing


@admin.register(Listing)
class ListingsAdmin(admin.ModelAdmin):
    list_display = ('club', 'pk', 'for_age_group', 'licence_required', 'telephone_number', 'created_at', 'author')
    list_filter = ('for_age_group', 'licence_required', 'created_at')