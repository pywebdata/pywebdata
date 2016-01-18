from lib.graph import Graph
import lib.search as search

class Topology(object):
    def __init__(self):
        self._graph = Graph()
        self._graph.directed = True

    def connect(self, u, v):
        self._graph.add_edge(u, v)

    def read_input(self, input_dict):
        """Creates a copy of the input dictionary to the topology"""
        self._params = input_dict.copy()

    def run(self):
        """Checks if the topology is cyclic. If so, do not run the topology and inform the user."""
        search.initialize(self._graph)
        search.topological_sort(self._graph)
        for service in reversed(search.processed_stack):
            # Note [0] at the end. Temporarily run just one query.
            output = service.query(**self._params)[0]
            service.update_parameters(**output)
            self._params.update(output)
