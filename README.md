WeatherAPI


This is a simple Flask-RestX API that manages weather data. The API allows users to upload weather data for a city and view the weather of a particular city.

Prerequisites

Python
Virtual Environment
Flask-RestX library

Installation

Clone the repository:

git clone https://github.com/Gabriel-kalango/weather-report.git

Navigate to the project directory:

Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate 

 # On Windows use `venv\Scripts\activate`

Install dependencies:


pip install -r requirements.txt

Create a .env file with the following content:


DEBUG=True

SECRET_KEY="create_a_secret_key"

FLASK_APP=runserver.py

Initialize and migrate the database:


flask db init

flask db migrate

flask db upgrade

Running the API

Start the server:


flask run

The app will be available at http://127.0.0.1:5000.

Using the AP
I
POST Endpoint

To add weather data for a city:

URL: http://127.0.0.1:5000/weather

Method: POST

Example data input:

{
    "city": "New York",
    "temperature": 25.5,
    "description": "Sunny"
}

You can use tools like Postman or Insomnia to make this request.

GET Endpoint

To get weather data for a specific city:

URL: http://127.0.0.1:5000/weather/<city name>

Method: GET

You can use tools like Postman or Insomnia to make this request.

Running Tests

To run tests on the endpoint:


pytest API/test/test_weather.py

Contact

For any questions or issues, please contact: kallythegreat11@gmail.com.