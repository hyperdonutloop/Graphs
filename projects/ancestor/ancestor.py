from util import Queue

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
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError('ERROR: No such Vertex exist.')

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])
    # do a BFS (storing the path)
    q = Queue()
    # enqueue a path to starting node
    q.enqueue([starting_node])
    # creating a set to store visited
    visited = set()
    # no parents set to -1
    # initializing parents
    parents = -1
    while q.size() > 0:
        # gets the first path in the queue
        path = q.dequeue()
        # getting last node in the path
        v = path[-1]
        # check if it has been visited, and if not ->
        if v not in visited:
            #mark it as visited
            visited.add(v)
            # check if path(v) is less than parent meaning if there was no path it would be the parent
            # or length is longer than 1
            if ((v < parents) or (len(path) > 1)):
                # update V with the new NODE
                parents = v
            # enqueue a path to all its neighbors
            for neighbor in g.get_neighbors(v):
                # make a copy of the path
                copy = path.copy()
                # append the neighbor
                copy.append(neighbor)
                # enqueue the copy
                q.enqueue(copy)
    return parents

