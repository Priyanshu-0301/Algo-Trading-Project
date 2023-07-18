#code to get Access token
import logging
import kiteSettings
from kiteconnect import KiteConnect

logging.basicConfig(level = logging.DEBUG)

kite = KiteConnect(kiteSettings.api_key)

# https://kite.zerodha.com/connect/login?v=4&api_key=Q8JPzjkt8ftXgqvmXa

request_token = input("Request_token: ")
data = kite.generate_session(request_token,kiteSettings.api_secret)
kite.set_access_token(data["access_token"])

print("--------")
print("Access Token: ", data["access_token"])