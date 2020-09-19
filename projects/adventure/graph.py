class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = self.vertices[vertex_id]

        return neighbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = []
        queue = []

        queue.append(starting_vertex)
        visited.append(starting_vertex)

        while queue:
            starting_vertex = queue.pop(0)
            print(starting_vertex, end=' ')

            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = []
        stack = []
        path = []

        stack.append(starting_vertex)

        while (len(stack)):
            starting_vertex = stack[-1]
            stack.pop()

            if starting_vertex not in visited:
                path.append(starting_vertex)
                visited.append(starting_vertex)

            n_list = sorted(self.get_neighbors(starting_vertex), reverse=False)
            for neighbor in n_list:
                if neighbor not in visited:
                    stack.append(neighbor)
        return path

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex not in visited:
            print(starting_vertex, end=' ')
            visited.append(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = []
        queue = []
        path = []

        if starting_vertex == destination_vertex:
            path.append(starting_vertex)
            path.append(destination_vertex)
            return path

        queue.append([starting_vertex])

        while queue:
            path = queue.pop(0)
            v = path[-1]
            if v not in visited:
                for neighbor in self.get_neighbors(v):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
                        if neighbor == destination_vertex:
                            return new_path
                visited.append(v)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = []
        stack = []
        path = []
        new_path = []

        if starting_vertex == destination_vertex:
            path.append(starting_vertex)
            path.append(destination_vertex)
            return path

        stack.append([starting_vertex])

        while (len(stack)):
            path = stack[-1]
            stack.pop()
            v = path[-1]
            new_path.append(v)

            if v not in visited:
                visited.append(v)

            for neighbor in self.get_neighbors(v):
                if neighbor not in visited:
                    stack.append([neighbor])
                    if neighbor == destination_vertex:
                        new_path.append(neighbor)
                        return new_path
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[], path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.append(starting_vertex)
        path.append(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, destination_vertex, visited, path)

        if path[-1] == destination_vertex:
            return path
        path.pop()
        visited.append(starting_vertex)
