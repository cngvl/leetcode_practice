from collections import deque

search_queue = deque()
graph = {}
search_queue += graph["you"]

def person_is_seller(name):
    return name[-1] == 'm'

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(f'{person} + "is a mango seller"')
        # return True
    else:
        search_queue += graph[person]
