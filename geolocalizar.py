# Primeiramente devemos importar as bibliotecas que vamos utilizar
import httplib2
import json

# Vamos criar nossa função
def geoLocalizar(localidade):

    # A função deve converter a string 'localidade' em dados de latitude e longitude
    chave_google = "AIzaSyAiJlGlnGS9xo_WoI8B4Nzzohvd0m6NPCA"
    
    # Documentação da Geocoding API do Google: https://developers.google.com/maps/documentation/geocoding/start?hl=pt-br
    # Vimos que a url troca espaço ' ' por '+' então devemos substituir.
    localidade = localidade.replace(" ", "+")

    # Formatar a Url com o formato especificado na documentação da API
    # FORMATO: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(localidade, chave_google)

    # httplib2 especifica como fazermos a requisição
    # Documentação httplib2: https://github.com/httplib2/httplib2
    h = httplib2.Http()

    # API da bilbioteca json que importamos: https://docs.python.org/3/library/json.html
    # O método loads() transforma a string JSON em um objeto python correspondente, ou seja, um dicionário
    content = json.loads(h.request(url, 'GET')[1].decode('utf-8'))

    latitude  = content['results'][0]['geometry']['location']['lat']
    longitude = content['results'][0]['geometry']['location']['lng']

    return (latitude, longitude)

''' 
from geoLocalizar import GeoLocalizar
GeoLocalizar("porto velho")
 '''