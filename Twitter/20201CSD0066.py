import sys
import string
import json
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    
    text = text.lower() #This function is used to convert all the input text into lower case characters.
    tokens = tokenizer.tokenize(text) #Used to reduce all the input text into smaller tokens
    return [token for token in tokens if token not in stopwords and not token.isdigit()] #filters out all the stop words that carry no meaning.

def normalize_contractions(tokens):
    token_map = {
        "i'm": "i am",
        "you're": "you are",
        "it's": "it is",
        "we're": "we are",
        "we'll": "we will",
        "i'll": "i will"
    } #define all word contractions
    for tok in tokens:
        #This function checks for word contractions and divides it into two words.
        #Each of these words will be tokenized seperately by using split function.
        if tok in token_map.keys():
            for item in token_map[tok].split():
                yield item
        else:
            yield tok
    
tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
print(punct)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
#creates a list of punctuation marks, stopwords, and combines them as a stopwords list for text processing tasks involving tweets or other text data.


tf = Counter() #Keeping a count of term frequencies
with open("home_timeline.jsonl", 'r') as f:
    #Processes a JSONL file, calculates the term frequencies of the tokens in the 'text' field of each tweet, prints the most common tokens, and creates a bar plot showing the term distribution and saved as 'term_distribution.png'.
    for line in f:
        tweet = json.loads(line)
        tokens = process(text=tweet.get('text', ''),
                            tokenizer=tweet_tokenizer,
                            stopwords=stopword_list)
        tf.update(tokens)
    y = [count for tag, count in tf.most_common(20)]
    x = range(1, len(y)+1)
    for tag, count in tf.most_common(40):
        print("{}: {}".format(tag, count))
    
    plt.bar(x, y)
    plt.title("Term Frequencies")
    plt.ylabel("Frequency")
    plt.savefig('term_distribution.png')