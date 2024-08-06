from flask_restx import Resource
from ..models import Weather
from ..schema import weatherNameSpace,weatherSerializer


@weatherNameSpace.route("")
class PostWeatherUpdate(Resource):

    @weatherNameSpace.expect(weatherSerializer)

    def post(self):
        """ creating weather update"""
        try:
            data=weatherNameSpace.payload
            city=data.get("city")
            temperature=data.get("temperature")
            description=data.get("description")
            if not city or not temperature or not description:
                return {"message": "Missing required fields"}, 400
        
            new_weather_report=Weather(city=city,temperature=temperature,description=description)
            new_weather_report.save()
            return  weatherNameSpace.marshal(new_weather_report, weatherSerializer),201
        except Exception as e:
            print(f"An error occurred: {e}")

            return {"message": "An error occurred while creating the weather report"}, 500


@weatherNameSpace.route("/<city>")
class GetWeatherUpdate(Resource):
    def get(self,city):
            weatherUpdate=Weather.query.filter(Weather.city==city).first()
            if weatherUpdate is not None:
                return  weatherNameSpace.marshal(weatherUpdate, weatherSerializer),200
            else:
                 return {"message":"this city data is not on the database"},404
        


