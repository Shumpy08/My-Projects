import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "KK5YFAA9HMI6WVIT"
NEWS_API_KEY = "149a4687238e4389afc03cabade0efec"
ACCOUNT_SID = "ACb763b94e0b2db1f83c7e517e21ff4275"
AUTH_TOKEN = "294e5d8c8d61619b3a8d1d661c574692"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]
print(yesterdays_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

up_down = ""
difference = (float(yesterdays_closing_price) - float(day_before_yesterday_closing_price))
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference_percent = (difference / float(yesterdays_closing_price)) * 100
print(difference_percent)

if abs(difference_percent) > 0.4:
    print("Get News")
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)

    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    abs_difference = abs(difference_percent)
    formatted_article = [f"{STOCK_NAME}: {up_down}{round(abs_difference)}, \nHeadline: {article['title']}, \nBrief: {article['description']}"
                         for article in three_articles]
    print(list)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_article:
        message = client.messages.create(
            to="+917781950588",
            from_="+15162593601",
            body=article

        )

# Optional TODO: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
