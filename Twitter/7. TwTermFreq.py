# Chap02/twitter_term_frequency.py
import sys
import string
import json
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [token for token in tokens if token not in stopwords and not token.isdigit()]

def normalize_contractions(tokens):
    token_map = {"i'm": "i am","you're": "you are","it's": "it is","we're": "we are","we'll": "we will","i'll": "i will"}
    for tok in tokens:
        if tok in token_map.keys():
            for item in token_map[tok].split():
                yield item
        else:
            yield tok

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
print(punct)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']

tf = Counter()
with open("home_timeline.jsonl", 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = process(text=tweet.get('text', ''),
                            tokenizer=tweet_tokenizer,
                            stopwords=stopword_list)
        tf.update(tokens)
    for tag, count in tf.most_common(40):
        print("{}: {}".format(tag, count))