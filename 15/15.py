import re

# Part 1
with open(r'/home/macolella/AoC2022/15/input') as f:
    readings = f.read().splitlines()

sensor_x = []
sensor_y = []
beacon_x = []
beacon_y = []
for reading in readings:
    coords_re = re.match('Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', reading.strip())
    sensor_x.append(int(coords_re.group(1)))
    sensor_y.append(int(coords_re.group(2)))
    beacon_x.append(int(coords_re.group(3)))
    beacon_y.append(int(coords_re.group(4)))

manhattan_dists = []
for ind in range(len(sensor_x)):
    manhattan_dists.append(abs(sensor_x[ind] - beacon_x[ind]) + abs(sensor_y[ind] - beacon_y[ind]))

beacons = set()
for ind in range(len(beacon_x)):
    beacons.add((beacon_x[ind], beacon_y[ind]))

checked_row = 2_000_000
no_beacons = set()
for sensor_ind, dist in enumerate(manhattan_dists):
    ubound = sensor_y[sensor_ind] + dist
    lbound = sensor_y[sensor_ind] - dist
    if lbound <= checked_row and ubound >= checked_row:
        adj_dist_y = checked_row - sensor_y[sensor_ind]
        adj_dist_x_pos = dist - abs(adj_dist_y)
        adj_dist_x_neg = -adj_dist_x_pos
        for i in range(adj_dist_x_neg, adj_dist_x_pos + 1):
            no_beacons.add((sensor_x[sensor_ind] + i, sensor_y[sensor_ind] + adj_dist_y))

no_beacons = no_beacons - beacons

print(f'The answer to Part 1 is {len(no_beacons)}')

# Part 2
coord_min = 0
coord_max = 4_000_000

def add_segment(start, end, segments):
    # Is this segment equal to or contained in another segment?
    for a, b in segments:
        if start >= a and end <= b:
            return

    # Does this segment enclose any other segments?
    for s in reversed(range(len(segments))):
        a, b = segments[s]
        if start <= a and end >= b:
            del segments[s]      # remove from from the list

    # Does this segment extend any segment to the left?
    for s in reversed(range(len(segments))):
        a, b = segments[s]
        if end >= (a-1) and end <= b:
            del segments[s]
            end = b             # new segment ends at old, but starts at start

    # Does this segment extend any segment to the right?
    for s in reversed(range(len(segments))):
        a, b = segments[s]
        if start >= a and start <= (b+1):
            del segments[s]
            start = a             # new segment starts at old, but ends at end

    # Add new segment to the list
    segments.append((start,end))
    return

def check_coverage(row):
    segments = []
    for sensor_ind, dist in enumerate(manhattan_dists):
        if abs(row - sensor_y[sensor_ind]) <= dist:
            start = (sensor_x[sensor_ind] - dist) + abs(row - sensor_y[sensor_ind])
            end = (sensor_x[sensor_ind] + dist) - abs(row - sensor_y[sensor_ind])
            if ((end >= coord_min) and (start <= coord_max)):
                start = max(start, coord_min)
                end = min(end, coord_max)
                add_segment(start, end, segments)
    return segments

for row in reversed(range(coord_min, coord_max + 1)):
    segments = check_coverage(row)
    if len(segments) > 1:
        break

start1, end1 = segments[0]
start2, end2 = segments[1]
if end1 + 2 == start2:
    x_coord = end1 + 1
elif end2 + 2 == start1:
    x_coord = end2 + 1

print(f'The answer to Part 2 is {coord_max*x_coord + row}')