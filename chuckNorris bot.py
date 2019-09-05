import requests
from twilio.rest import Client


chuck = requests.get("https://api.chucknorris.io/jokes/random").json()

account_sid='ACac4f74cc1fb204c6b5fcb7a7972a6594'
auth_token = '0c37236a305b7eea40c1f83736fbfcfc'
client = Client(account_sid, auth_token)
client.messages.create(body=chuck['value'], from_='+13302788823', to='+13303048971')
    
