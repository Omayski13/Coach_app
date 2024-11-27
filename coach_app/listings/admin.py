from django.contrib import admin

from coach_app.listings.models import Listing


# Register your models here.

@admin.register(Listing)
class ListingsAdmin(admin.ModelAdmin):
    list_display = ('pk','club','for_age_group','licence_required','telephone_number','created_at','author')
    list_filter = ('for_age_group','licence_required','created_at')