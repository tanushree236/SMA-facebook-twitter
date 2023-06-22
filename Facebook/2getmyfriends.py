import facebook
import json

token = "EABTDSezqk1sBAJa2WFhINhB11tAXzZBD1r9RnUoQnIxmBxluGjacZBZAKSY1pvxmpXbaAPpEAz2HxiW3QaU5RxNmjLhb9WcJZCTvZC41SLdP4C1ZBmOYanReUamR2JZCiqZBpFo82qlkalbdVnrlwz7z9zJhE7J6XRbwHOZCd461DTEqgtQLjcGMfz0HT5h4hNQLZA5oxnAveTpWAhzMMZAKITkNwqDbRS8mS1JV8EBJtRuS4ix2LgPfhUP"
graph = facebook.GraphAPI(token)
user = graph.get_object("me")
friends = graph.get_connections(user["id"],"friends")
list = [friend['name'] for friend in friends['data']]
print(json.dumps(friends, indent=4))
print(json.dumps(list))