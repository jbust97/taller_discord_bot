import requests
from decouple import config
def get_description(name):
    url = "http://www.omdbapi.com/"
    query = {"t": name,"apikey":config("API_KEY")}
    response = requests.get(url,params=query)
    movie = response.json()
    return movie["Plot"]
def get_movie(name):
    url = "http://www.omdbapi.com/"
    query = {"t": name,"apikey":config("API_KEY")}
    response = requests.get(url,params=query)
    movie = response.json()
    return movie