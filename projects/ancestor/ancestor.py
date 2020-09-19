from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    v_list = []

    for vertices in ancestors:
        v_list.append(vertices[0])
        v_list.append(vertices[1])
    v_set = set(v_list)
    for v in v_set:
        graph.add_vertex(v)
    for vertices in ancestors:
        graph.add_edge(vertices[1], vertices[0])

    p_list = graph.dft(starting_node)

    if len(p_list) < 2:
        end_node = -1
    else:
        end_node = p_list[len(p_list) - 1]
    return end_node

"""
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))  # 10)
print(earliest_ancestor(test_ancestors, 2))  # -1)
print(earliest_ancestor(test_ancestors, 3))  # 10)
print(earliest_ancestor(test_ancestors, 4))  # -1)
print(earliest_ancestor(test_ancestors, 5))  # 4)
print(earliest_ancestor(test_ancestors, 6))  # 10)
print(earliest_ancestor(test_ancestors, 7))  # 4)
print(earliest_ancestor(test_ancestors, 8))  # 4)
print(earliest_ancestor(test_ancestors, 9))  # 4)
print(earliest_ancestor(test_ancestors, 10))  # -1)
print(earliest_ancestor(test_ancestors, 11))  # -1)
"""
