# Django and Scrapy Integration with LLM-Enhanced Functionality

This project integrates **Django** and **Scrapy** to process and enhance hotel data using a **Large Language Model (LLM)** powered by **Ollama**. The system is designed to scrape hotel data, store it in a PostgreSQL database, and use Django CLI commands to generate rewritten titles, summaries, ratings, and reviews for hotels. The rewritten data is stored in additional database tables for further use.

## Features

- **Hotel Data Scraping:**
  - Uses Scrapy to scrape hotel data and populate a PostgreSQL database.

- **Django-Based Data Processing:**
  - Processes hotel data using Django management commands.
  - Enhances data using Ollama’s LLM API for generating titles, summaries, ratings, and reviews.

- **PostgreSQL Integration:**
  - Centralized database to store scraped and processed data.

- **Test Suite:**
  - Comprehensive tests for Django models, services, and CLI commands.
  - Integration of `pytest` for testing with coverage reporting.

## Project Structure

```
assignment-10/
├── llm_handler/                # Django project directory
│   ├── core/                  # Core settings and configurations
│   ├── property_app/          # Django app for managing hotel data
│   │   ├── models.py          # Models for hotel data and processed data
│   │   ├── services/          # API services (e.g., Ollama integration)
│   │   ├── management/        # Custom Django CLI commands
│   │   │   └── commands/
│   │   │       └── generate_hotel_data.py
│   │   ├── tests/             # Unit tests for the application
│   └── manage.py
├── scrapy_project/             # Scrapy project directory
│   ├── spiders/               # Scrapy spiders for scraping hotel data
│   ├── pipelines.py           # Pipelines to process scraped data
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Dockerfile for the project
├── requirements.txt            # Python dependencies
├── pytest.ini                  # pytest configuration
└── README.md                   # Project documentation (this file)
```

## Prerequisites

- **Docker** and **Docker Compose**
- **Python 3.11**
- PostgreSQL (for the database)

## Installation

### Clone the Repository
```bash
git clone https://github.com/arman-007/assignment-10.git
cd assignment-10
```

### Configure Environment Variables
Create a `.env` file in the root directory and configure the following:
```
DATABASE_URL=postgresql://myuser:mypassword@db:5432/hotel_db
```

### Build Docker Containers
To build the containers:
```bash
docker compose build
```
## Usage
### Run database container
After the containers are built, let's start the database.
To start the database container in detach mode:
```bash
docker compose up db -d
```

### Start Scrapy to populate the database
Once the database is up and running, start the scrapy service:
```bash
docker compose up scrapy -d
```
This will populate the `hotels` table with necessary scraped data needed.

### Start Ollama container
The `hotels` table data are required for LLM to process. to start the LLM container:
```bash
docker compose up ollama -d
```
Once the `ollama` container is running, an ollama model is needed to be pulled.
To get inside the `ollama` container:
```bash
docker exec -it ollama bash
```
let's pull the `llama3.2:1b` model:
```bash
ollama run llama3.2:1b
```

### Get Django CLI in action
To run the django container:
```bash
docker compose up django -d
```

Get inside the `django` container to migration, migrate and execute the CLI.
- To get inside `django` container:
```bash
docker exec -it property_rewriter bash
```
- redirect to Django project directory:
```bash
cd llm_handler
```
- to do the migrations and migrate:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
- Once the tbales are created, the CLI command can be runa nd store the responses. To run the CLI command:
```bash
python manage.py generate_hotel_data
```
This command will:
- Fetch hotel data from the database.
- Send it to Ollama’s LLM for enhancement.
- Store the generated titles, summaries, ratings, and reviews in corresponding tables.

## Testing

### Run Tests
Execute the test suite using `pytest` inside django project directory (inside `llm_handler` folder):
```bash
pytest --cov=property_app --cov-report=term
```

## Key Components

### Models
- **`Hotel`**: Stores raw hotel data.
- **`GeneratedTitle`**: Stores generated titles.
- **`HotelSummary`**: Stores generated summaries.
- **`HotelRating`**: Stores generated ratings and reviews.

### Django CLI Command
- **`generate_hotel_data`**:
  - Fetches data from the `Hotel` table.
  - Sends data to Ollama LLM.
  - Saves processed data to `GeneratedTitle`, `HotelSummary`, and `HotelRating` tables.

### Scrapy
- Scrapes hotel details and populates the PostgreSQL database.

### Ollama LLM Integration
- Calls Ollama’s API to process and enhance hotel data.

