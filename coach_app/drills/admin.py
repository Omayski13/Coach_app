from django.contrib import admin

from coach_app.drills.models import Drill


@admin.register(Drill)
class DrillAdmin(admin.ModelAdmin):
    list_display = ('name','approved', 'focus', 'for_age_group','objectives', 'author','created_at')
    list_filter = ('approved','created_at', 'focus', 'for_age_group','author',)
