import requests

query = input("What type of news are you interested in? ")

url = "https://newsdata.io/api/1/latest"

params = {
    "apikey": "pub_e3c68d9a3a824598af4781b9ab1c510c",
    "q": query,
    "language": "en"
}

response = requests.get(url, params=params)

news = response.json()

if news.get("status") == "success":
    for article in news["results"]:
        print(article.get("title"))
        print(article.get("description"))
        print('-------------------------------------------------')
else:
    print("API Error:", news)