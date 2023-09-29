import requests
from send_email import send_email


api_key = "8b2eb8f64426448093a856a735e1cc58"
topic = "tesla"


url1 = f"https://newsapi.org/v2/everything?\
q={topic}\
&sortBy=publishedAt\
&apiKey=8b2eb8f64426448093a856a735e1cc58\
&language=en"

req = requests.get(url1)
content = req.json()

body = ""+"Subject: Today's News"+2*'\n'
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + '\n'+article["description"]+'\n'+ article["url"]+2*'\n'

# encoding error solved
body = body.encode("utf-8")

send_email(body)

# print(body)