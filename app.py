import time
from RandomQuote import RandomQuote
import requests
import sched

# TO-DO: Prevent quote from changing on refresh when time is not due
scheduler = sched.scheduler(time.time, time.sleep)


def fetch_random_quote():
    url = "https://api.quotable.io/quotes/random"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            quotes = response.json()
            for quote in quotes:
                content = quote.get("content")
                author = quote.get("author")
                random_quote = RandomQuote(content, author)
                print(random_quote)
        else:
            print("failed to fetch a quote")
    except Exception as e:
        return f"Error: {e}"


def task():
    scheduler.enter(0, 1, fetch_random_quote, ())
    scheduler.enter(60, 1, task, ())


task()
scheduler.run()
