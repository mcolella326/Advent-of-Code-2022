import re
from collections import deque, defaultdict
from itertools import permutations, combinations

with open(r'/home/macolella/AoC2022/16/input') as f:
    valve_map = f.read().splitlines()

# Part 1

# Parsing
valve_dict = {}
for line in valve_map:
    line_re = re.match(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    valve = line_re.group(1)
    rate = line_re.group(2)
    neighbors = line_re.group(3).split(', ')
    valve_dict[valve] = {'rate' : int(rate), 'neighbors' : neighbors, 'dist' : {}}

# BFS to generate distance map among all openable nodes + starting node
flow_valves = [valve for valve in valve_dict.keys() if valve_dict[valve]['rate'] != 0 or valve == 'AA']

def bfs_dist(start, end):
    q = deque()
    visited = set()
    q.append([start])
    while q:
        path = q.popleft()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            if node == end:
                valve_dict[start]['dist'][end] = len(path)
                return
            for neighbor in valve_dict[node]['neighbors']:
                if neighbor not in visited:
                    path_copy = path[:]
                    path_copy.append(neighbor)
                    q.append(path_copy)

for start_valve, end_valve in permutations(flow_valves, 2):
    bfs_dist(start_valve, end_valve)

# BFS to open all openable valves in min time
def bfs_time(flow_valves, time_allotted):
    q = deque()
    visited_states = set()
    max_relief_dict = defaultdict(lambda: None)
    q.append([('AA', time_allotted, 0, frozenset())])
    while q:
        path = q.popleft()
        state = path[-1]
        if state not in visited_states:
            visited_states.add(state)
            remaining_flow_valves = flow_valves - state[3]
            for valve in remaining_flow_valves:
                node, time_remaining, total_relief, opened_valves = state
                opened_valves = set(opened_valves)
                if ((new_time := time_remaining - valve_dict[node]['dist'][valve]) > 0):
                    opened_valves.add(valve)
                    opened_valves = frozenset(opened_valves)
                    total_relief += new_time*valve_dict[valve]['rate']
                    new_state = (valve, new_time, total_relief, opened_valves)
                    if not max_relief_dict[opened_valves]:
                        max_relief_dict[opened_valves] = total_relief
                    if new_state not in visited_states:
                        if total_relief >= max_relief_dict[opened_valves]:
                            path_copy = path[:]
                            path_copy.append(new_state)
                            q.append(path_copy)
                            max_relief_dict[opened_valves] = total_relief
    return max_relief_dict

flow_valves.remove('AA')
flow_valves = frozenset(flow_valves)
max_relief_dict = bfs_time(flow_valves, 30)
print(f'The answer to Part 1 is {max(max_relief_dict.values())}')

# Part 2
max_relief_dict = bfs_time(flow_valves, 26)
possible_combos = [max_relief_dict[me] + max_relief_dict[elephant] for me, elephant in 
    combinations(max_relief_dict.keys(), 2) if me.isdisjoint(elephant)]

print(f'The answer to Part 2 is {max(possible_combos)}')