from collections import deque

discovered = {}
processed = {}
parents = {}

def initialize(graph):
    global finished
    finished = False

    for v in graph.vertices:
        discovered[v] = False
        processed[v] = False
        parents[v] = None

def dfs(graph, vertex):
    if finished:
        return

    discovered[vertex] = True
    edge = graph.edges[vertex]
    while edge:
        v = edge.endpoint
        if not discovered[v]:
            discovered[v] = True
            parents[v] = vertex
            dfs(graph, v)
        edge = edge.next
    process_vertex(vertex)
    processed[vertex] = True

processed_stack = deque()
def process_vertex(v):
    processed_stack.append(v)

finished = False
def process_edge(u, v):
    global finished
# Check if this routine is correct.
# Compare with Skiena.
    if discovered[v]:
        print 'Cycle from %s to %s' %(v, u)
        find_path(v, u, parents)
        finished = True

def find_path(start, end, parents):
    if start == end or end == None:
        print start
    else:
        find_path(start, parents[end], parents)
        print end

def topological_sort(graph):
    """Returns the root of the input graph"""
    for v in graph.vertices:
        if not discovered[v]:
            dfs(graph, v)
    for v in processed_stack:
        pass
    return v
