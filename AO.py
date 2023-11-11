def Cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)  # Use max instead of min for OR condition
        cost[Path_B] = PathB
    return cost

def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        condition = Conditions[key]
        c = Cost(H, condition, weight)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, condition, weight)
    return least_cost

def shortest_path(Start, Updated_cost, H):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)
         
        # FIND MINIMIMUM PATH KEY
        Next = key[Index].split()
        # ADD TO PATH FOR OR PATH
        if len(Next) == 1:
            Start = Next[0]
            Path += ' --> ' + shortest_path(Start, Updated_cost, H)
        # ADD TO PATH FOR AND PATH
        else:
            Path += '-->(' + key[Index] + ') '
            Start = Next[0]
            Path += '[' + shortest_path(Start, Updated_cost, H) + ' + '
            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, H) + ']'
    return Path

def get_user_defined_heuristics():
    H = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter heuristic values for nodes:")
    for i in range(num_nodes):
        node = input(f"Node {i+1}: ")
        heuristic_value = int(input(f"Heuristic value for {node}: "))
        H[node] = heuristic_value
    return H

def get_user_defined_conditions():
    Conditions = {}
    num_conditions = int(input("Enter the number of conditions: "))
    print("Enter conditions in the following format:")
    print("For AND condition: A AND B")
    print("For OR condition: A OR B")
    for i in range(num_conditions):
        node = input(f"Enter node for condition {i+1}: ")
        condition = input(f"Enter condition for node {node}: ")
        condition_type, nodes = condition.split(' ', 1)
        nodes = nodes.split()
        if node in Conditions:
            Conditions[node][condition_type] = nodes
        else:
            Conditions[node] = {condition_type: nodes}
    return Conditions

def initial_cost(H, Conditions, weight=1):
    initial_costs = {}
    for key, condition in Conditions.items():
        initial_costs[key] = Cost(H, condition, weight)
    return initial_costs

H1 = get_user_defined_heuristics()
Conditions = get_user_defined_conditions()

# weight
weight = 1

# Initial cost
initial_costs = initial_cost(H1, Conditions, weight)
print("-" * 45)
print(f"{'Node':<10}{'Initial Value':<15}{'Updated Value':<15}")
print("-" * 45)
for node, cost in initial_costs.items():
    print(f"{node:<10}{H1[node]:<15}{cost[list(cost.keys())[0]]:<15}")
print('*' * 75)

# Updated cost
print('Updated Cost:')
Updated_cost = update_cost(H1, Conditions, weight)
for key, cost in Updated_cost.items():
    print(f'{key}: {cost}')
print('*' * 75)

# Shortest path
print('Shortest Path:\n', shortest_path('A', Updated_cost,H1))
