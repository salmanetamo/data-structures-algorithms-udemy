class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = dict()

    def add_vertex(self, node):
        if node in self.adjacency_list.keys():
            return False
        self.adjacency_list[node] = []
        self.number_of_nodes += 1
        return True

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list.keys() or node2 not in self.adjacency_list.keys():
            return False
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

        return True

    def show_connections(self):
        for node in self.adjacency_list.keys():
            print(str(node) + ' --> ', end='')
            for neighbour in self.adjacency_list[node]:
                print('\t' + str(neighbour), end='')
            print()


# Tests
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')
graph.show_connections()