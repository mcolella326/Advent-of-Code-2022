import re
from collections import deque, defaultdict

with open(r'/home/macolella/AoC2022/19/input') as f:
    blueprints = f.read().splitlines()

# Part 1

# Parsing (1 == ORE, 2 == CLAY, 3 == OBSIDIAN, 4 == GEODE)
blueprint_dict = {}
for blueprint in blueprints:
    costs_re = re.match(r'''Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.''', blueprint)
    blueprint_num = costs_re.group(1)
    ore_robot_ore_cost = costs_re.group(2)
    clay_robot_ore_cost = costs_re.group(3)
    obs_robot_ore_cost = costs_re.group(4)
    obs_robot_clay_cost = costs_re.group(5)
    geo_robot_ore_cost = costs_re.group(6)
    geo_robot_obs_cost = costs_re.group(7)
    blueprint_dict[int(blueprint_num)] = {1 : {1 : int(ore_robot_ore_cost)}, 
                                    2 : {1 : int(clay_robot_ore_cost)},
                                    3 : {1 : int(obs_robot_ore_cost), 2 : int(obs_robot_clay_cost)},
                                    4 : {1 : int(geo_robot_ore_cost), 3 : int(geo_robot_obs_cost)}
                                    }

initial_robots = {1 : 1, 2 : 0, 3 : 0, 4 : 0}
initial_resources = {1 : 0, 2 : 0, 3 : 0, 4 : 0}

# Function returning the min possible resources needed to create a robot for each resource
def get_max_robots(bp_num):
    max_robots = {1 : 0, 2 : 0, 3 : 0, 4 : 1000}
    for _, requirements in bp_num.items():
        for robot_type, qty in requirements.items():
            max_robots[robot_type] = max(max_robots[robot_type], qty)
    return max_robots

# Function returning the potential robot building options given current resources
def get_build_options(bp_num, resources):
    options = {0}
    for robot, requirements in bp_num.items():
        if all(qty <= resources[robot] for robot, qty in requirements.items()):
            options.add(robot)
    if 4 in options:
        return {4}
    return options

# Function collecting resources at the end of each timestep
def collect(robots, resources):
    for robot_type, robot_num in robots.items():
        resources[robot_type] += robot_num
    return resources

# Function returning new robots and reources based on building a robot this timestep
def build_robot(bp_num, robots, resources, to_build):
    robots[to_build] += 1
    for resource, qty in bp_num[to_build].items():
        resources[resource] -= qty
    return (robots, resources)

# DFS through each blueprint
def dfs(bp_num, time_allotted):
    stack = deque()
    timestep = 0
    skipped_prev_iter = set()
    stack.append((timestep, initial_robots, initial_resources, skipped_prev_iter))
    best_at_timestep = defaultdict(int)
    max_robots = get_max_robots(bp_num)
    while stack:
        timestep, robots, resources, skipped_last_iteration = stack.popleft()
        best_at_timestep[timestep] = max(best_at_timestep[timestep], resources[4])
        if timestep <= time_allotted and best_at_timestep[timestep] == resources[4]:
            options = get_build_options(bp_num, resources)
            for to_build in options:
                if not to_build:
                    new_resources = collect(robots, resources.copy())
                    stack.append((timestep + 1, robots, new_resources, options))
                elif to_build in skipped_last_iteration:
                    continue
                elif robots[to_build] + 1 > max_robots[to_build]:
                    continue
                else:
                    new_robots, new_resources = build_robot(bp_num, robots.copy(), resources.copy(), to_build)
                    new_resources = collect(robots, new_resources.copy())
                    stack.appendleft((timestep + 1, new_robots, new_resources, set()))
    return best_at_timestep[time_allotted]

part1 = sum([i * dfs(bp_num, 24) for i, bp_num in blueprint_dict.items()])
print(f'The answer to Part 1 is {part1}')

# Part 2
largest_geodes = [dfs(bp_num, 32) for bp_num in list(blueprint_dict.values())[:3]]
part2 = 1
for geode in largest_geodes:
    part2 *= geode
print(f'The answer to Part 2 is {part2}')