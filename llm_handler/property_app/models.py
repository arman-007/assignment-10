from django.db import models


class Hotel(models.Model):
    id = models.BigAutoField(primary_key=True)  # Match the `id` column type
    property_title = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    location = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    room_type = models.TextField()
    price = models.FloatField()
    city_name = models.TextField()

    class Meta:
        db_table = 'hotels'  # Use the existing table name
        managed = True       # Allow Django to manage this table


class GeneratedTitle(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, primary_key=True)
    generated_title = models.TextField()


class HotelSummary(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, primary_key=True)
    summary = models.TextField()


class HotelRating(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, primary_key=True)
    rating = models.TextField()
    review = models.TextField()
