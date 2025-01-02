import pytest
from property_app.models import Hotel, GeneratedTitle, HotelSummary, HotelRating

@pytest.mark.django_db
class TestGeneratedTitle:
    def test_generated_title_creation(self):
        # Create a Hotel instance
        hotel = Hotel.objects.create(
            property_title="Test Hotel",
            rating=4.5,
            location="Test Location",
            latitude=45.0,
            longitude=-93.0,
            room_type="Deluxe",
            price=200.0,
            city_name="Test City"
        )
        # Create a GeneratedTitle instance
        generated_title = GeneratedTitle.objects.create(
            hotel=hotel,
            generated_title="Test Generated Title"
        )
        # Assertions
        assert generated_title.generated_title == "Test Generated Title"
        assert generated_title.hotel == hotel

    def test_generated_title_update(self):
        # Create a Hotel instance
        hotel = Hotel.objects.create(
            property_title="Test Hotel",
            rating=4.5,
            location="Test Location",
            latitude=45.0,
            longitude=-93.0,
            room_type="Deluxe",
            price=200.0,
            city_name="Test City"
        )
        # Create and update a GeneratedTitle instance
        generated_title = GeneratedTitle.objects.create(
            hotel=hotel,
            generated_title="Old Title"
        )
        generated_title.generated_title = "Updated Title"
        generated_title.save()
        # Assertions
        assert generated_title.generated_title == "Updated Title"


@pytest.mark.django_db
class TestHotelSummary:
    def test_hotel_summary_creation(self):
        # Create a Hotel instance
        hotel = Hotel.objects.create(
            property_title="Test Hotel",
            rating=4.5,
            location="Test Location",
            latitude=45.0,
            longitude=-93.0,
            room_type="Deluxe",
            price=200.0,
            city_name="Test City"
        )
        # Create a HotelSummary instance
        summary = HotelSummary.objects.create(
            hotel=hotel,
            summary="Test Summary"
        )
        # Assertions
        assert summary.summary == "Test Summary"
        assert summary.hotel == hotel


@pytest.mark.django_db
class TestHotelRating:
    def test_hotel_rating_creation(self):
        # Create a Hotel instance
        hotel = Hotel.objects.create(
            property_title="Test Hotel",
            rating=4.5,
            location="Test Location",
            latitude=45.0,
            longitude=-93.0,
            room_type="Deluxe",
            price=200.0,
            city_name="Test City"
        )
        # Create a HotelRating instance
        rating = HotelRating.objects.create(
            hotel=hotel,
            rating="5",
            review="Great place!"
        )
        # Assertions
        assert rating.rating == "5"
        assert rating.review == "Great place!"
        assert rating.hotel == hotel
