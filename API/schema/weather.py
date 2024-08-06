from flask_restx import fields,Namespace

weatherNameSpace=Namespace("weather",description="operations on weather")

weatherSerializer=weatherNameSpace.model("weather",{
    "id":fields.Integer(),
    "city":fields.String(required=True,description="the city of the weather update"),
    "date":fields.Date(dt_format='rfc822',description="time it was posted"),
    "temperature":fields.Float(required=True,description="the temperature of the city"),
    "description":fields.String(required=True,description="describing the weather condition")
    
})