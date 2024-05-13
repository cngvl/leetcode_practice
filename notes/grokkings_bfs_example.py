from collections import deque

# search_queue = deque()
# graph = {}
# search_queue += graph["you"]

def person_is_seller(name):
    # Example checking if the person is a seller
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    graph = {
        'You': ['Alice', 'Bob', 'Claire'],
        'Bob': ['Anuj', 'Peggy'],
        'Alice': ['Peggy'],
        'Claire': ['Thom', 'Jonny'],
        'Anuj': [],
        'Peggy': [],
        'Thom': [],
        'Jonny': []
    }
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("You"))
