import requests
import json
query=input("what type of new you are interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-02-28&sortBy=publishedAt&apiKey=9fafe868d7194436a00c3bc80340667d"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------")