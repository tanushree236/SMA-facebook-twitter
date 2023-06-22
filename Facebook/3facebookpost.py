import json
import facebook
import requests

token="EABTDSezqk1sBAFefc1nrefeMtuy2Tw7f0ECyZChWLcaA8V5oU07uzLZAF7unNHvMZB9SMaRJViQVoM71p6IIBuVLAuFMcC3RhQCB2jcD1dqGwWjZBM8TtAXDP72Y3tRofkIDz6Ng3xowx0jID9RZBL9wuaLY7V0c9awzMVTgoeTQsY3ZAIqWm4nB9ionhYRQb9LRtCpjBelCcyuC4ZC7ZBQ1d8pEPnwcG8jYeNlDjt8ojbR5BqZCCn7st"
graph = facebook.GraphAPI(token)
posts = graph.get_connections("me", 'posts', fields='message,created_time,description,caption,link,place,status_type,shares')

with open('my_posts.jsonl', 'a') as f:
    for post in posts['data']:
        f.write(json.dumps(post)+"\n")
    posts = requests.get(posts['paging']['next']).json()
     