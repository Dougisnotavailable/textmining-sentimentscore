from textblob import TextBlob
from newspaper import Article 
import nltk


url = 'https://edition.cnn.com/2022/06/09/us/uvalde-texas-shooting-officers-classroom/index.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)


#get the clean text and pass the strings
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # range -1 to 1. 
print("The sentiment score of this page is: " + str(sentiment) )

if sentiment > 0.15:
    print("This website emanate very positive vibes")
elif sentiment > 0.00:
    print("Kinda neutral but ok")
elif sentiment > -0.15:
    print("Evil walks through these realms")
else:
    print("This website is pure evil")
