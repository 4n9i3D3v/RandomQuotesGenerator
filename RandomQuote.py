from datetime import date


class RandomQuote:

    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __str__(self):
        # return f"\n*** Quote of the day: {date.today().strftime("%B %d %Y")} *** \n '{self.content}' \n \t\t~ by {
        # self.author}"
        return f"\n*** New Quote *** \n '{self.content}' \n \t\t~ by {self.author}"
