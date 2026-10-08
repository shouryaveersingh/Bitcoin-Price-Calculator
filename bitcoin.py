
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin_value = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")

try:
    respone = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apikey=5a0469cc06b4a70542d1e1380b1302812f9c210675a331f18c308c44c4419486")
    bitcoin_price = float(respone.json()["data"]["priceUsd"])
    result = bitcoin_value * bitcoin_price
    print(f"${result:,.4f}")
except requests.RequestException:
    pass
