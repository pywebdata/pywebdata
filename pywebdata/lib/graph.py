from collections import defaultdict

class EdgeNode(object):
    def __init__(self, endpoint, weight = 0):
        self.endpoint = endpoint
        self.next = None
        self.weight = weight

    def __str__(self):
        if self is None:
            return 'EdgeNode None'
        else:
            return 'EdgeNode %s' % self.endpoint

class Graph(object):
    def __init__(self):
        self.edges = defaultdict(lambda: None)
        self.vertices = []
        self.degrees = defaultdict(int)
        self.n_vertices = 0
        self.n_edges = 0
        self.directed = False

    def __str__(self):
        string = ''
        for vertex in self.vertices:
            string = ''.join([string, 'Node %s, ' %vertex])
            edge = self.edges[vertex]
            string = ''.join([string, 'Neighbors:'])
            while edge:
                string = ''.join([string, ' ', str(edge.endpoint)])
                edge = edge.next
            string += '\n'
        return string

    def add_edge(self, origin, dest, weight = 0):
        for v in [origin, dest]:
            if v not in self.vertices:
                self.vertices.append(v)

        if origin not in self.edges:
            self.edges[origin] = None
            self.degrees[origin] = 0
            self.n_vertices += 1
        if dest not in self.edges:
            self.edges[dest] = None
            self.degrees[dest] = 0
            self.n_vertices += 1

        edge = EdgeNode(dest, weight)
        edge.next = self.edges[origin]
        self.edges[origin] = edge
        self.degrees[origin] += 1
        self.n_edges += 1

        if not self.directed:
            edge = EdgeNode(origin)
            edge.next = self.edges[dest]
            self.edges[dest] = edge
            self.degrees[dest] += 1

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.edges[vertex] = None
