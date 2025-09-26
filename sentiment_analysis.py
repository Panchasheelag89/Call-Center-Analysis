from textblob import TextBlob  # simple library sentiment ke liye

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity>0: return "Positive"
    elif polarity<0: return "Negative"
    else: return "Neutral"


