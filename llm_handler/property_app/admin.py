from django.contrib import admin
from .models import Hotel, GeneratedTitle, HotelSummary, HotelRating

# Admin class for the unmanaged Hotel model
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_title', 'rating', 'location', 'price', 'city_name')
    search_fields = ('property_title', 'city_name', 'location')
    list_filter = ('city_name', 'room_type', 'rating')
    ordering = ('id',)

# Admin class for GeneratedTitle
@admin.register(GeneratedTitle)
class GeneratedTitleAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'generated_title')
    search_fields = ('hotel__property_title', 'generated_title')
    ordering = ('hotel',)

# Admin class for HotelSummary
@admin.register(HotelSummary)
class HotelSummaryAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'summary')
    search_fields = ('hotel__property_title', 'summary')
    ordering = ('hotel',)

# Admin class for HotelRating
@admin.register(HotelRating)
class HotelRatingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'rating', 'review')
    search_fields = ('hotel__property_title', 'review')
    list_filter = ('rating',)
    ordering = ('hotel',)
