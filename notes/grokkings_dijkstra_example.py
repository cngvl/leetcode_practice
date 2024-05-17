# Graph HashMaps
# Setting up initial HashMap
graph = {}

# Setting up the start node
graph["start"] = {}

# Assigning edges and costs for the start node
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# Assigning edges and costs for the A node
graph["a"]["fin"] = 1

# Assigning edges and costs for the B node
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# Cost HashMaps
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

# Parents HashMap
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Processed nodes
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    # Getting the cost and neighbours of the node in interest
    cost = costs[node]
    neighbors = graph[node]

    # Loop through it's neighbours
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Comparison to see if the newly calculated cost is 'cheaper' than it's previous cost
        if costs[n] > new_cost:
            # If so, update the cost to the 'cheaper' value and also 'remember' how to get to the node
            costs[n] = new_cost
            parents[n] = node
    # Add to the list of nodes visited
    processed.append(node)
    # Restart the loop
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
print(processed)
