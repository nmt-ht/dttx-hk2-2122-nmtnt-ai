from collections import defaultdict
print("BFS - DFS for graph 2 \n")

with open("source\input_graph2.txt") as f:
    lines = f.read().strip().split("\n")

graph = defaultdict(list)

for line in lines:
    ls = line.split(" ")
    graph[ls[0]] = ls[1:]

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

startNode = 's'
endNode = 'g'

def printResult(result):
  if(result is not None):
    print(result)
  else:
    print("No path found.")

def bfs(visited, graph, start, destionation): #function for BFS
  visited.append(start)
  queue.append(start)

  while queue:          # Creating loop to visit each node
    vertice = queue.pop(0) 
    if(vertice == destionation or len(vertice) == 0):
      return visited

    for neighbour in graph[vertice]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search:")
result = bfs(visited, graph, startNode, endNode)
printResult(result)

print("\n")

class Stack:
    def __init__(self):
        self.list = []

    def add(self,item):
        if item:
            self.list.append(item)

    def pop(self):
        if len(self.list) == 0: return None
        last_item = self.list[-1]
        del(self.list[-1])
        return last_item

    def print(self):
        print(self.list)

    def is_empty(self):
        return len(self.list) == 0

stack = Stack()
def dfs(visited, graph, start, destination):
    stack.add(start)
    visited.add(start)
    path = []
    while stack.is_empty() == False:
        vertex = stack.pop()
        path.append(vertex)

        if len(vertex) == 0 or vertex == destination:
            return path
        
        visited.add(vertex)
        for neighbor in graph[vertex]:
          if neighbor not in visited:
              stack.add(neighbor)

# Driver Code
print("Following is the Depth-First Search:")
result = dfs(set(), graph, startNode, endNode)
printResult(result)
