'''
Author: Oliver S. Lee
Last Modified: 05/06/2024

Description:
A basic implementation of a graph. The backing structure is a dictionary/map, where
the key is the starting node and the value is the ending node. In this implementation
the edges do have a direction.

Also contains implementations of several useful graph algorithms
'''

# Imports
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_edge(self, start_node, end_node):
        if start_node not in self.adj_list:
            self.adj_list[start_node] = [end_node]
        else:
            self.adj_list[start_node].append(end_node)
            
    def show_edges(self):
        for node in self.adj_list:
            print(node, '->', self.adj_list[node])
            
def dfs(graph, start_node):
    visited_set = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited_set:
            visited_set.add(node)
            print(node)
            
            if node in graph.adj_list:
                for neighbor in graph.adj_list[node]:
                    if neighbor not in visited_set:
                        stack.append(neighbor)

def bfs(graph, start_node):
    visited_set = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited_set:
            visited_set.add(node)
            print(node)
            
            if node in graph.adj_list:
                for neighbor in graph.adj_list[node]:
                    if neighbor not in visited_set:
                        queue.append(neighbor)
                        
if __name__ == "__main__":
    # Testing the graph and DFS
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'A')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'A')
    g.add_edge('C', 'F')
    g.add_edge('D', 'B')
    g.add_edge('E', 'B')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')
    g.add_edge('F', 'E')

    print("Graph:")
    g.show_edges()

    print("\nDFS(A):")
    dfs(g, 'A')
    
    print("\nBFS(A):")
    bfs(g, 'A')