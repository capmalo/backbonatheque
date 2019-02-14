from django.contrib import admin

from .models import MajorPlayback


@admin.register(MajorPlayback)
class MajorPlaybackAdmin(admin.ModelAdmin):
    fields = ("date_updated", "date_created", "status", "album", "customer")
    readonly_fields = ("date_updated", "date_created")
