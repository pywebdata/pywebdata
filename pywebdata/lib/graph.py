class EdgeNode(object):
    def __init__(self, endpoint, weight = 0):
        self.endpoint = endpoint
        self.next = None
        self.weight = weight

    def __str__(self):
        if self is None:
            return 'EdgeNode None'
        else:
            return 'EdgeNode %s' % self.data

class Graph(object):
    def __init__(self):
        self.edges = {}
        self.degrees = {}
        self.n_vertices = 0
        self.n_edges = 0
        self.directed = False

    def __str__(self):
        '''print_graph in the book'''
        string = ''
        for key in self.edges.keys():
            string = ''.join([string, 'Node %s, ' %key])
            edge = self.edges[key]
            string = ''.join([string, 'Neighbors:'])
            while edge:
                string = ''.join([string, ' ', str(edge.endpoint)])
                edge = edge.next
            string += '\n'
        return string

    def add_edge(self, origin, dest, weight = 0):
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
