from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from heapq import heappop, heappush


def get_exits(room_id):
    """
    Get all exits (edges) of a room.
    """
    exits = traversal_graph[room_id]
    return exits


def heuristic(start_room, end_room):
    return abs(start_room.x - end_room.x) + abs(start_room.y - end_room.y)


def astar(room_id):
    open = []
    closed = []

    open.append(room_id)

    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        for exit in get_exits(current_node):
            if traversal_graph[current_node][exit] == '?':
                path = []
                while traversal_graph[current_node][exit] != room_id:
                    path.append(traversal_graph[current_node][exit])
                    # current_node = player.travel(opposite[exit])
                return path[::-1]

        for exit in get_exits():
            if traversal_graph[current_node][exit] in closed:
                continue

        g = heuristic(neighbor_id, current_node)
        h = heuristic(neighbor_id, end_id)
        f = g + h
        # if (room_id in open) and f >= f):
            # open.append(room_id)

    return None

def bfs(room_id):
    """
    Return a list containing the shortest path from
    starting_vertex to ? in
    breath-first order.
    """
    visited = []
    queue = []
    path = []

    queue.append([room_id])

    while queue:
        path = queue.pop(0)
        v = path[-1]
        if v not in visited:
            for exit in get_exits(v):
                if traversal_graph[v][exit] not in visited:
                    new_path = list(path)
                    new_path.append(traversal_graph[v][exit])
                    queue.append(new_path)
                    if traversal_graph[v][exit] == '?':
                        new_path.pop()
                        return new_path
            visited.append(v)
    return None


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Initialize lists and dictionaries
traversal_path = []
opposite = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
traversal_graph = {}
dir_dict = {}
end = False
first_room = True

# Initialize the starting room
player.current_room = world.starting_room

# Initialize the exits for the starting room
exit_list = player.current_room.get_exits()
for exit in exit_list:
    dir_dict[exit] = '?'
    current_room = player.current_room.id
traversal_graph[current_room] = dir_dict

# Pick a random direction, traverse it and add the traversal

while end is False:
    dir_list = []
    for k, v in traversal_graph[current_room].items():
        if v == '?':
            dir_list.append(k)

    if first_room is True:
        direction = 'w'
        first_room = False
    else:
        direction = random.choice(dir_list)

    while direction in traversal_graph[current_room].keys():
        print('Current Room = ', current_room, 'Dir = ', direction)
        if traversal_graph[current_room][direction] == '?':
            old_room = current_room
            player.travel(direction)
            traversal_path.append(direction)
            traversal_graph[current_room][direction] = player.current_room.id
            current_room = player.current_room.id
            exit_list = player.current_room.get_exits()

            if current_room not in traversal_graph:
                dir_dict = {}
                for exit in exit_list:
                    dir_dict[exit] = '?'
                    traversal_graph[current_room] = dir_dict
            traversal_graph[current_room][opposite[direction]] = old_room
        else:
            dir_list = []
            for k, v in traversal_graph[current_room].items():
                if v == '?':
                    dir_list.append(k)

            direction = random.choice(dir_list)

    # Find the shortest route to an unexplored room and convert to directions
    back_path = []
    shortest_path = bfs(current_room)
    print(shortest_path)
    print(traversal_graph)
    if shortest_path is None:
        end = True
        break
    for i in range(len(shortest_path) - 1):
        for key, value in traversal_graph[shortest_path[i]].items():
            if value == shortest_path[i+1]:
                back_path.append(key)

    traversal_path = traversal_path + back_path
    print(traversal_path)
    print(len(traversal_path))

    for d in back_path:
        player.travel(d)
    current_room = player.current_room.id

print(traversal_path)
print('Length = ', len(traversal_path))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# print('Visted Rooms = ', visited_rooms)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
