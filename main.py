import requests
import time
from send_email import send_email

# Adjusting clock time to automate the task

clock = time.strftime("%Y-%m-%d")
print(clock)
clock = clock.split("-")
print(clock)
clock1 = int(clock[1])

if clock1 < 10:
 clock1 = clock1-1
 clock1 = "0"+str(clock1)

clock[1] = clock1
clock = "-".join(clock)
print(clock)

api_key = "8b2eb8f64426448093a856a735e1cc58"
url = f"https://newsapi.org/v2/everything?q=tesla&from=\
{clock}&sortBy=publishedAt&apiKey=\
8b2eb8f64426448093a856a735e1cc58"

req = requests.get(url)
content = req.json()

body = ""
i=0
for article in content["articles"]:
    if article["title"] is not None:
        i += 1
        body = body + f"{i} - {article['title']}"+ "\n" + article["description"] + 2*'\n'

# encoding error solved
body = body.encode("utf-8")

send_email(body)

# print(body)