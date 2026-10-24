from django.contrib import admin
from .models import ContactMessage, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "created")
    list_filter = ("category", "featured")
    search_fields = ("title", "tech")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "topic", "created", "handled")
    list_filter = ("topic", "handled")
    list_editable = ("handled",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("created",)
