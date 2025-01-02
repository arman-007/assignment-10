import logging
from django.core.management.base import BaseCommand
from property_app.models import Hotel, GeneratedTitle, HotelSummary, HotelRating
from property_app.services.ollama_service import call_ollama


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Generate rewritten titles, summaries, ratings, and reviews for hotels."

    def handle(self, *args, **kwargs):
        hotels = Hotel.objects.all()
        for hotel in hotels:
            # Create the prompt
            prompt = f"""
            Generate the following information based on the given hotel data:
            1. A rewritten title.
            2. A concise summary.
            3. A rating (between 1 to 5).
            4. A review.

            Hotel Data:
            Title: {hotel.property_title}
            Rating: {hotel.rating or 'N/A'}
            Location: {hotel.location}
            Latitude: {hotel.latitude or 'N/A'}
            Longitude: {hotel.longitude or 'N/A'}
            Room Type: {hotel.room_type}
            Price: {hotel.price}
            City: {hotel.city_name}

            Response Format (must follow strictly, 4 lines only, no blank new lines):
            Title: <Generated Title>
            Summary: <Generated Summary>
            Rating: <Generated Rating>
            Review: <Generated Review>
            """
            
            # Call Ollama API
            response = call_ollama(prompt)
            
            # Parse response
            try:
                lines = response.split("\n")
                generated_title = next(line.split(":")[1].strip() for line in lines if line.startswith("Title:"))
                summary = next(line.split(":")[1].strip() for line in lines if line.startswith("Summary:"))
                rating = next(line.split(":")[1].strip() for line in lines if line.startswith("Rating:"))
                review = next(line.split(":")[1].strip() for line in lines if line.startswith("Review:"))
            except (ValueError, StopIteration, IndexError) as e:
                logger.error(f"Failed to parse response for hotel {hotel.id}: {response}")
                continue
            
            # Save to GeneratedTitle table
            GeneratedTitle.objects.update_or_create(
                hotel=hotel,
                defaults={"generated_title": generated_title}
            )

            # Save to HotelSummary table
            HotelSummary.objects.update_or_create(
                hotel=hotel,
                defaults={"summary": summary}
            )

            # Save to HotelRating table
            HotelRating.objects.update_or_create(
                hotel=hotel,
                defaults={"rating": rating, "review": review}
            )

            self.stdout.write(self.style.SUCCESS(f"Processed hotel {hotel.id}: Title, Summary, Rating, Review"))