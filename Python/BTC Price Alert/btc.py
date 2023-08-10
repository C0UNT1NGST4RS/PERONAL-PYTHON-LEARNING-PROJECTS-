import requests

#11ce429b-0753-4e57-8a02-8b8a524a3ae5

#https://maker.ifttt.com/trigger/{event}/json/with/key/ySuwBqRyKm67WPwHetWe0

btc_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(btc_api_url)
response_json =response.json()
type(response_json)
response_json[0]
