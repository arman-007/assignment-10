from django.db import connection
from unittest.mock import patch, MagicMock
from django.core.management import call_command
from django.test import TransactionTestCase
from property_app.models import GeneratedTitle, HotelSummary, HotelRating

class TestGenerateHotelDataCommand(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create the `hotels` table
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS hotels (
                    id SERIAL PRIMARY KEY,
                    property_title TEXT NOT NULL,
                    rating FLOAT,
                    location TEXT NOT NULL,
                    latitude FLOAT,
                    longitude FLOAT,
                    room_type TEXT NOT NULL,
                    price FLOAT NOT NULL,
                    city_name TEXT NOT NULL,
                    image_url TEXT,
                    image_path TEXT
                )
            """)

    # @classmethod
    # def tearDownClass(cls):
    #     with connection.cursor() as cursor:
    #         cursor.execute("DROP TABLE IF EXISTS hotels")
    #     super().tearDownClass()


    def setUp(self):
        # Insert mock data
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM hotels")  # Clear any existing data
            cursor.execute("""
                INSERT INTO hotels (property_title, rating, location, latitude, longitude, room_type, price, city_name)
                VALUES
                ('Test Hotel', 4.5, 'Test Location', 45.0, -93.0, 'Deluxe', 200.0, 'Test City')
            """)

    @patch("property_app.management.commands.generate_hotel_data.call_ollama")
    def test_generate_hotel_data_success(self, mock_call_ollama):
        # Mock the call_ollama function to return a valid response
        mock_call_ollama.return_value = (
            "Title: Generated Test Hotel\n"
            "Summary: This is a generated summary.\n"
            "Rating: 5\n"
            "Review: This is a generated review."
        )

        # Run the management command
        call_command("generate_hotel_data")

        # Assertions
        self.assertTrue(GeneratedTitle.objects.filter(generated_title="Generated Test Hotel").exists())
        self.assertTrue(HotelSummary.objects.filter(summary="This is a generated summary.").exists())
        self.assertTrue(HotelRating.objects.filter(rating="5", review="This is a generated review.").exists())

    @patch("property_app.management.commands.generate_hotel_data.call_ollama")
    def test_generate_hotel_data_parsing_failure(self, mock_call_ollama):
        """
        Test the `generate_hotel_data` command when the API response cannot be parsed.
        """
        # Mock the call_ollama function to return an invalid response
        mock_call_ollama.return_value = "Invalid Response Format"

        # Reset the table and insert a mock Hotel instance
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE hotels RESTART IDENTITY CASCADE;")
            cursor.execute("""
                INSERT INTO hotels (property_title, rating, location, latitude, longitude, room_type, price, city_name)
                VALUES ('Test Hotel', 4.5, 'Test Location', 45.0, -93.0, 'Deluxe', 200.0, 'Test City')
                RETURNING id
            """)
            hotel_id = cursor.fetchone()[0]  # Fetch the auto-generated hotel ID

        # Run the command
        with self.assertLogs("property_app.management.commands.generate_hotel_data", level="ERROR") as log:
            call_command("generate_hotel_data")

        # Assert error log
        expected_message = f"Failed to parse response for hotel {hotel_id}: Invalid Response Format"
        self.assertIn(expected_message, log.output[0])

        # Ensure no data was saved to the database
        self.assertFalse(GeneratedTitle.objects.exists())
        self.assertFalse(HotelSummary.objects.exists())
        self.assertFalse(HotelRating.objects.exists())
