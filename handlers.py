from telegram.ext import CallbackContext
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from dotenv import load_dotenv
from text import weather
import requests
import os

load_dotenv()
API_KEY=os.getenv("API_KEY")

def start(update:Update, context:CallbackContext):
    user=update.effective_user.full_name
    update.message.reply_text(
        text=f"Hi {user}! ob-havoni ko'rsatishim uchun location tugmasini bosing:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Location",request_location=True)
                ]
            ],
            resize_keyboard=True
        )
    )
def send_weather(update:Update,context:CallbackContext):
    url="https://api.openweathermap.org/data/2.5/weather"
    location=update.message.location
    payload={
        "lat":location.latitude,
        "lon":location.longitude,
        "appid": API_KEY
    }
    response=requests.get(url,params=payload)
    data=response.json()
    if data['cod']==200:
        update.message.reply_text(
            text=weather.format(
                country=data['name'],
                description=data['weather'][0]['description'],
                temp=round(data['main']['temp'] -273.15,2),
                feels_like=round(data['main']['feels_like'] -273.15,2),
                cloud=data['clouds']['all'],
                humidity=data['main']['humidity'],
                wind_speed=data['wind']['speed'],
                pressure=data['main']['pressure']
            )
        )


