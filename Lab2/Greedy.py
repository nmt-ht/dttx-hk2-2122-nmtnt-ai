from collections import deque

class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes

    def greedy_algorithm(self, start_node, stop_node):
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
                if n == None or self.h[v] < self.h[n]:
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
            for (m) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n]

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n]:
                        g[m] = g[n]
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
    'A': ['C', 'D'],
    'B': ['D','E'],
    'C': ['G'],
    'D': ['G'],
    'E': [],
    'F': ['G'],
    'G': [],
    'S': ['B', 'A', 'F']
}

heuristic1 = {
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0,
    'S': 6
}

graph1 = Graph(adjacency_list_1, heuristic1)
print("Graph 1: ", adjacency_list_1)
print("\nGreedy from S to G")
graph1.greedy_algorithm('S', 'G')
print("--------------------------------------------------------------\n")

adjacency_list_2 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'k'],
    'd': ['b', 'e', 'm'],
    'e': ['d', 'n'],
    'f': ['s', 'p'],
    's': ['f', 'h'],
    'h': ['s', 'k'],
    'k': ['c', 'h'],
    'm': ['d', 'n', 'g'],
    'n': ['e', 'm'],
    'p': ['f', 'q'],
    'q': ['p', 'r'],
    'r': ['q', 't'],
    't': ['r', 'g'],
    'g': ['t']
}

heuristic2 = {
    'a': 4,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 3,
    'f': 5,
    's': 4,
    'h': 3,
    'k': 2,
    'm': 1,
    'n': 2,
    'p': 4,
    'q': 3,
    'r': 2,
    't': 1,
    'g': 0
}

print("Graph 2: ", adjacency_list_2)
graph3_1 = Graph(adjacency_list_2, heuristic2)
print("\nGreedy from s to g")
graph3_1.greedy_algorithm('s', 'g')
print("--------------------------------------------------------------\n")

adjacency_list_3 = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['B', 'A', 'D'],
    'D': ['F', 'E', 'G'],
    'E': ['G', 'D'],
    'F': ['D', 'G'],
    'G': ['E', 'D', 'G'],
}

heuristic3_1 = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0,
}

heuristic3_2 = {
    'A': 10,
    'B': 12,
    'C': 10,
    'D': 8,
    'E': 1,
    'F': 4.5,
    'G': 0,
}

print("Graph 3: ", adjacency_list_3)
graph3_1 = Graph(adjacency_list_3, heuristic3_1)
print("\nGreedy from A to G with h1")
graph3_1.greedy_algorithm('A', 'G')

graph3_2 = Graph(adjacency_list_3, heuristic3_2)
print("\nGreedy from A to G with h2")
graph3_2.greedy_algorithm('A', 'G')
print("--------------------------------------------------------------\n")

adjacency_list_4 = {
    'Arad': ['Zerind','Timisoara', 'Sibiu'],
    'Bucharest': ['Urziceni', 'Giurgiu', 'Pitesti', 'Fagaras'],
    'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
    'Dobreta': ['Craiova', 'Mehadia'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Neamt': ['Iasi'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti'],
    'Sibiu': ['Rimnicu Vilcea', 'Fagaras', 'Arad', 'Oradea'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Zerind': ['Arad', 'Oradea'],
}

heuristic4 = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea':193 ,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

print("Graph 4: ", adjacency_list_4)
graph4 = Graph(adjacency_list_4, heuristic4)
print("\nGreedy from Arad to Bucharest")
graph4.greedy_algorithm('Arad', 'Bucharest')
print("--------------------------------------------------------------\n")