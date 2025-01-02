import psycopg2
import os
from urllib.parse import urlparse

class HotelsPipeline:
    def process_item(self, item, spider):
        """
        Process each item and save it to the `hotels` table in the database.
        """
        self.save_to_db(item)
        return item

    def save_to_db(self, item):
        """
        Save the hotel data to the database.
        """
        # Get the database connection details from the environment variable
        db_url = os.getenv("DATABASE_URL")
        result = urlparse(db_url)
        db_params = {
            "dbname": result.path.lstrip("/"),
            "user": result.username,
            "password": result.password,
            "host": result.hostname,
            "port": result.port,
        }

        try:
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()

            # Insert the hotel data into the table
            cursor.execute("""
                INSERT INTO hotels (property_title, rating, location, latitude, longitude, room_type, price, city_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                item.get("property_title"),
                item.get("rating"),
                item.get("location"),
                item.get("latitude"),
                item.get("longitude"),
                item.get("room_type"),
                item.get("price"),
                item.get("city_name"),
            ))

            # Commit the transaction and close the connection
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            spider.logger.error(f"Error saving to database: {e}")
