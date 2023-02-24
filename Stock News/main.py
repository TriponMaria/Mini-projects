import datetime as dt
import requests
from twilio.rest import Client

percent_decrease = 0
percent_increase = 0

# alphavantage
API_KEY_ALPHAVANTAGE = "your api key - ALPHAVANTAGE "
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
STOCK_NAME = "TSLA"

# news
API_KEY_NEWSAPI ="your api key - NEWSAPI"
COMPANY_NAME = "tesla"
SORTBY = "popularity"

# twilio
account_sid = "your account_sid"
auth_token = "your auth_token"
client = Client(account_sid, auth_token)
message_text = f'\n{STOCK_NAME}:'
send = False

today = dt.date.today()
day1 = str(today - dt.timedelta(days=2))
day2 = str(today - dt.timedelta(days=1))

# Verify when STOCK_NAME price increase/decreases between yesterday and the day before yesterday
stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": API_KEY_ALPHAVANTAGE
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
closing_prices = {}
closing_prices[day1] = [float(data[day]["4. close"]) for day in data.keys() if day == day1]
closing_prices[day2] = [float(data[day]["4. close"]) for day in data.keys() if day == day2]
closing_price_day_1 = closing_prices[day1][0]
closing_price_day_2 = closing_prices[day2][0]

if closing_price_day_1 > closing_price_day_2:
    percent_decrease = 100 - 100 * closing_price_day_2 / closing_price_day_1
    message_text += "🔻"
else:
    percent_increase = 100 - 100 * closing_price_day_1 / closing_price_day_2
    message_text += "🔺"

# Use https://newsapi.org to get the first 3 news pieces for the COMPANY_NAME.
news_parameters = {
    "q": COMPANY_NAME,
    "from": str(today - dt.timedelta(days=1)),
    "to": str(today),
    "sortBy": SORTBY,
    "apiKey": API_KEY_NEWSAPI
}
response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
response.raise_for_status()
news = response.json()["articles"][:3]

news_dict = {}
news_dict["title"] = [n["title"] for n in news]
news_dict["description"] = [n["description"] for n in news]


# Verify when STOCK_NAME price increase/decreases by 5% or 2% between yesterday and the day before yesterday
# Send a seperate message with the percentage change and each article's title and description to your phone number.
for i in range(3):
    message_news = ''
    if percent_decrease >= 5 or percent_increase >= 5:
        message_news += f"5%\nHeadline: {news_dict['title'][i]}\nBrief:{news_dict['description'][i]}"
        send = True
    elif percent_decrease >= 2 or percent_increase >= 2:
        message_news += f"2%\nHeadline: {news_dict['title'][i]}\nBrief:{news_dict['description'][i]}"
        send = True
    if send:
        message = client.messages \
            .create(
            body=message_text + message_news,
            from_='your twilio phone number',
            to='your phone number'
        )

