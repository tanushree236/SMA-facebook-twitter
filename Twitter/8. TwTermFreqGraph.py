import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
print(punct)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']

if len(sys.argv)!=2:
    sys.exit()
fname = sys.argv[1]
tf = Counter()
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = process(text=tweet.get('text', ''),
                            tokenizer=tweet_tokenizer,
                            stopwords=stopword_list)
        tf.update(tokens)
    y = [count for tag, count in tf.most_common(20)]
    x = range(1, len(y)+1)

    plt.bar(x, y)
    plt.title("Term Frequencies")
    plt.ylabel("Frequency")

    plt.savefig('term_distribution.png')