from geolocalizar import geoLocalizar
import json
import httplib2

import sys
import codecs

#Código padrão do python 3 para permitir acentos nas Strings
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

''' Siga os passos em https://developer.foursquare.com/docs/api/getting-started
E cole aqui seus IDs, lembre-se, tem que criar um app, pode colocar uma url 
 que não existe!
'''
fclient_id = "GO14AXXYW5IXVMLRCISKVAJRM0TROTYRVUOZXB4P1B0NWZIJ"
fclient_secret = "XLB5NXYS1YYQ5G1DPPLFJ0AJAXGVKZIENYICOBZKI3R43LRC"


def acharRestaurante(tipoComida,localidade):
    # Usando o geolocalizar para pegar latitude e longitude do Google Maps!
    # Lembre-se que para importar o arquivo precisa estar na mesma pasta que este aqui!!!!
    latitude, longitude = geoLocalizar(localidade)
    # Usando a API do foursquare para encontrar o restaurante mais próximo com as strings latitude, longitude e tipo de comida.
    # Lendo a documentação, o formato da url é nesse estilo https://api.foursquare.com/v2/venues/search?client_id=GO14AXXYW5IXVMLRCISKVAJRM0TROTYRVUOZXB4P1B0NWZIJ&client_secret=XLB5NXYS1YYQ5G1DPPLFJ0AJAXGVKZIENYICOBZKI3R43LRC&v=20130815&ll=40.7,-74&query=sushi
    # então...

    #url = "https://api.foursquare.com/v2/venues/search?client_id=GO14AXXYW5IXVMLRCISKVAJRM0TROTYRVUOZXB4P1B0NWZIJ&client_secret=XLB5NXYS1YYQ5G1DPPLFJ0AJAXGVKZIENYICOBZKI3R43LRC&v=20130815&ll=40.7,-74&query=sushi"
    url = "https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20130815&ll={},{}&query={}".format(fclient_id, fclient_secret, latitude, longitude, tipoComida)

    
    #1. Faça você a requisição, lembre-se dos comandos padrões
    h =  httplib2.Http() # preencha aqui
    result = json.loads(h.request(url, 'GET')[1].decode('utf-8')) # preencha aqui

    #print(result['response']['venues'][2])
    # Seguindo a documentação da foursquare 'venues' são os locais
    if result['response']['venues']:

    #       #2.  Achando o primeiro restaurante - FAÇA VOCÊ
        restaurant = result['response']['venues'][0]#analise a variável result e pegue o primeiro dado

        
    #     # Armazenando o nome e endereço

    
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
       
        

        #Formatando o Endereço
        address = ""
        
        for i in restaurant_address:
            address += i + " "

        restaurant_address = address
        restaurantInfo = {'name':restaurant_name, 'address':restaurant_address}
        
        # # Mostrando os resultados
        print("Restaurant Name: %s" % (restaurantInfo['name']))
        print("Restaurant Address: %s" % (restaurantInfo['address']))
        #return restaurantInfo

        print("\nRestaurante: {}".format(restaurant_name))
        print("Endereço   : {}".format(restaurant_address))
    # else:
    #       print("No Restaurants Found for %s" % (location))
    #       return "No Restaurants Found"

if __name__ == '__main__':
    #3. Rode aqui a função, mude o tipo de comida e a localização para testar
    acharRestaurante("Pizza", "porto velho, brasil")
