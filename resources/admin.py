from django.contrib import admin
from .models import Resource, Booking

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'resource_type', 'capacity')
    list_filter = ('resource_type',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('resource', 'user', 'start_time', 'end_time', 'status', 'assigned_staff')
    list_filter = ('status', 'resource')
    search_fields = ('user__username', 'resource__name')
    # This allows the Dept. Head to quickly change status in the list view
    list_editable = ('status', 'assigned_staff')