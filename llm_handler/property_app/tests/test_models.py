# import pytest
# from property_app.models import GeneratedTitle, HotelSummary, HotelRating

# @pytest.mark.django_db
# class TestGeneratedTitle:
#     def test_generated_title_creation(self):
#         # Create a mock Hotel instance
#         hotel_id = 1  # Use an arbitrary ID for mocking
#         generated_title = GeneratedTitle.objects.create(
#             hotel_id=hotel_id,
#             generated_title="Test Generated Title"
#         )
#         # Assertions
#         assert generated_title.generated_title == "Test Generated Title"
#         assert generated_title.hotel_id == hotel_id

#     def test_generated_title_update(self):
#         hotel_id = 1
#         generated_title = GeneratedTitle.objects.create(
#             hotel_id=hotel_id,
#             generated_title="Old Title"
#         )
#         # Update the generated title
#         generated_title.generated_title = "Updated Title"
#         generated_title.save()
#         assert generated_title.generated_title == "Updated Title"

# @pytest.mark.django_db
# class TestHotelSummary:
#     def test_hotel_summary_creation(self):
#         hotel_id = 2  # Use an arbitrary ID for mocking
#         summary = HotelSummary.objects.create(
#             hotel_id=hotel_id,
#             summary="Test Summary"
#         )
#         # Assertions
#         assert summary.summary == "Test Summary"
#         assert summary.hotel_id == hotel_id

# @pytest.mark.django_db
# class TestHotelRating:
#     def test_hotel_rating_creation(self):
#         hotel_id = 3  # Use an arbitrary ID for mocking
#         rating = HotelRating.objects.create(
#             hotel_id=hotel_id,
#             rating="5",
#             review="Great place!"
#         )
#         # Assertions
#         assert rating.rating == "5"
#         assert rating.review == "Great place!"
#         assert rating.hotel_id == hotel_id
