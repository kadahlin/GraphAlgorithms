#Kyle Dahlin

#Implementation of the Bellman Ford algorithm for single source shortest paths

import sys
import math
from Graph import Graph

def bellman_ford(graph: Graph, starting_node: str):
	"""
	Runs the bellman ford algorithm on Grap graph starting at starting_node.
	Returns the distance and previous vectors. Note that this implementation does
	not detect negative cycles but it does correctly handle negative edges
	"""
	distance = {}
	previous = {}

	for node in graph.get_nodes():
		distance[node] = math.inf
		previous[node] = None

	distance[starting_node] = 0

	for x in range(len(graph.get_nodes()) - 1):
		for node in graph.get_nodes():
			for edge in graph.get_edges(node):
				if distance[node] + edge[1] < distance[edge[0]]:
					distance[edge[0]] = distance[node] + edge[1]
					previous[edge[0]] = node

	return (distance, previous)

def print_shortest_paths(graph, distance, previous, starting_node):
	"""
	Constructs and prints the shortest path for each node in graph g
	from the starting node
	"""
	for node in sorted(graph.get_nodes()):
		path = []
		current_node = node
		while current_node != None:
			path.insert(0, current_node)
			current_node = previous[current_node]
		print("Node {} can be reached via {} at a cost of {}".format(
			node, ' -> '.join(path), distance[node]))

if __name__ == '__main__':
	#Take a kgraph file and a state node as a parameter
	#Kgraphs are explained in Graph.py
	g = Graph(sys.argv[1])
	d,p = bellman_ford(g, sys.argv[2])
	print_shortest_paths(g, d, p, sys.argv[2])