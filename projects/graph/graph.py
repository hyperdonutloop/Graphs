"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enqueue a path to starting vertex ID
        # adding the starting node to a queue
        q.enqueue(starting_vertex)

        #create a set to keep track of visited verticies
        visited = set()
        # while set is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if it is not visited
            if v not in visited:
                print(v)
                # mark visited
                visited.add(v)
                # enqueue all of it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store the visited verticies
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop the first vertex
            #
            v = s.pop()
            # checking to see if it's visited,
            # if it has not been visited
            if v not in visited:
                print(v)
                # mark it as visited
                visited.add(v)
                # push all of it's neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)



    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if the node has been visited
        if visited is None:
            # this is a set to store visited vertices
            visited = set()
        print(starting_vertex)
        # mark it as visited
        visited.add(starting_vertex)
        # call the function on each neighbor vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if each neighbor is not in visited
            if neighbor not in visited:
                # call the function again with neighbors
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        q = Queue()
        # enqueue A PATH TO the starting vertex
        # whatever starting vertex is I am adding to the queue
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            # removing something equals the path
            path = q.dequeue()
            # grab the vertex from the end of the path
            v = path[-1]
            # check if it's not been visited
            # if it has not been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # check if it's the target
                if v == destination_vertex:
                    # if it is the target
                    return path
                # enqueue a path to all the neighbors
                for neighbor in self.get_neighbors(v):
                    # make a duplicate of the path
                    copy = path.copy()
                    # append the neighbor
                    copy.append(neighbor)
                    # enqueue the copy
                    q.enqueue(copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()
        # push a PATH TO the starting vertex
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # get the vertex from the end of the path
            v = path[-1]
            # check if it has been visited
            # if it has not been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # check if it is the target
                if v == destination_vertex:
                    # if it is the target
                    return path
                # push a path to all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    copy = path.copy()
                    # append the neighbor
                    copy.append(neighbor)
                    # push the copy
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # check if the node has been visited
        if visited is None:
            # create a set to store the visited vertices
            visited = set()
        # check if path exists
        if path is None:
            path = []
        # mark it as visited
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # check to see if we are at the destination
        if starting_vertex == destination_vertex:
            # if it is then return the path
            return path
        # call the function on each neighbor. THIS IS THE RECURSION
        for neighbor in self.get_neighbors(starting_vertex):
            # if the neighbor is not in the visited set
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # if items are within the new_path, return it
                if new_path is not None:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
