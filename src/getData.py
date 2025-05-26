import yfinance as yf       # free and open source python library to scrape from yahoo finance
ticker = yf.Ticker("AAPL")
options_dates = ticker.options # an array of the dates of our options
chain = ticker.option_chain(options_dates[0]) # this has heaps of info
print(chain.calls.head()) # this is a pandas df, of the options being traded
currentPrice = ticker.info["regularMarketPrice"]
print(f"Current AAPL stock price: ${currentPrice}")

# we can use tickers for multiple tickers data
# we can use market
