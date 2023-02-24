1. Use https://www.alphavantage.co
2. Verify when STOCK_NAME price increase/decreases by 5% or %2 between yesterday and the day before yesterday
3. Use https://newsapi.org to get the first 3 news pieces for the COMPANY_NAME
4. When STOCK_NAME price increase/decreases by 5% or 2% between yesterday and the day before yesterday then send a seperate message with the percentage change and each article's title and description to your phone number, using https://www.twilio.com
Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
