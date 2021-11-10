import tweepy
import json

# Autentificación a la API
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Inicialización de la API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Parametros para la busqueda de tweets
numberOfTweets = 6
keyword = "Tweetestj"

# Listas para guardar las ubicaciones de los tweets
places = []
placesNames = []
latitude = []
longitude = []

# Búsqueda de tweets con palabra/frase clave
for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode="extended").items(numberOfTweets):
  if tweet.place != None:
    places.append(tweet.place)
    placesNames.append(tweet.place.name)
    latitude.append(tweet.place.bounding_box.coordinates[0][0][1])
    longitude.append(tweet.place.bounding_box.coordinates[0][0][0])

# Imprimir los resultados
for item in places:
  print(item.name)
  print(item.bounding_box.coordinates[0][0])


count = 0

# Se guardan las coordenadas en un archivo .txt resultcoordinates.txt con estructura de csv
with open('resultcoordinates.txt', 'w') as resultsc:
    resultsc.write('%s\n' % "Longitud,Latitud")
    while count < numberOfTweets:
      resultsc.write('%s\n' % (str(longitude[count]) + "," + str(latitude[count])))
      count += 1
