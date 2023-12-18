import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()
API_KEY=os.getenv("API_KEY")

def test():
    
    url="https://api.openweathermap.org/data/2.5/weather?lat=0.2&lon=0.55&appid=e103948f1d6901c91a9f0781706e976b"

    response=requests.get(url)
    data=response.json()['weather'][0]['description']
    pprint(data)
test()
