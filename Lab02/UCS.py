from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes

    def ucs_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        countOpenedNode = 0

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] < g[n]:
                    n = v
                    countOpenedNode = countOpenedNode + 1

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                print("Opened node: ", countOpenedNode)
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list_1 = {
    'A': [('C', 2), ('D', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'E': [],
    'F': [('G', 6)],
    'G': [],
    'S': [('B', 1), ('A', 2), ('F', 3)]
}


graph1 = Graph(adjacency_list_1)
print("Graph 1: ", adjacency_list_1)
print("\nUCS from S to G")
graph1.ucs_algorithm('S', 'G')
print("--------------------------------------------------------------\n")

adjacency_list_2 = {
    'a': [('b', 5), ('c', 3)],
    'b': [('a', 4), ('d', 6)],
    'c': [('a', 4), ('k', 2)],
    'd': [('b', 5), ('e', 7), ('m', 7)],
    'e': [('d', 6), ('n', 8)],
    'f': [('s', 0), ('p', 2)],
    's': [('f', 1), ('h', 1)],
    'h': [('s', 0), ('k', 2)],
    'k': [('c', 3), ('h', 3)],
    'm': [('d', 7), ('n', 8), ('g', 6)],
    'n': [('e', 7), ('m', 7)],
    'p': [('f', 1), ('q', 3)],
    'q': [('p', 2), ('r', 4)],
    'r': [('q', 3), ('t', 5)],
    't': [('r', 4), ('g', 6)],
    'g': [('t', 5)]
}

print("Graph 2: ", adjacency_list_2)
graph2 = Graph(adjacency_list_2)
print("\nUCS from s to g")
graph2.ucs_algorithm('s', 'g')
print("--------------------------------------------------------------\n")

adjacency_list_3 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 1), ('D', 5)],
    'C': [('B', 1), ('A', 4), ('D', 3)],
    'D': [('F', 3), ('E', 8), ('G', 9)],
    'E': [('G', 2), ('D', 8)],
    'F': [('D', 3), ('G', 5)],
    'G': [('E', 2), ('D', 3), ('G', 9)],
}

print("Graph 3: ", adjacency_list_3)
graph3_1 = Graph(adjacency_list_3)
print("\nUCS from A to G with h1")
graph3_1.ucs_algorithm('A', 'G')

graph3_2 = Graph(adjacency_list_3)
print("\nUCS from A to G with h2")
graph3_2.ucs_algorithm('A', 'G')
print("--------------------------------------------------------------\n")

adjacency_list_4 = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Bucharest': [('Urziceni', 85), ('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97)],
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagaras', 99), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Iasi', 92), ('Urziceni',142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
}

print("Graph 4: ", adjacency_list_4)
graph4 = Graph(adjacency_list_4)
print("\nUCS from Arad to Bucharest")
graph4.ucs_algorithm('Arad', 'Bucharest')
print("--------------------------------------------------------------\n")