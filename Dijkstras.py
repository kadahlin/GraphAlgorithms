#Kyle Dahlin

#Implemention of Dijkstras single source shortest paths algorithm.

import sys
import math
from Graph import Graph

def get_min_distance_node(distance: dict, s: set):
	"""
	Return the node from s that has the minimum value in the distance dictionary
	"""
	min_node = None
	min_cost = math.inf
	for node in s:
		if distance[node] < min_cost:
			min_node = node
			min_cost = distance[node]
	return min_node


def dijkstras(graph: Graph, start_node: str):
	"""
	Perform single source dijkstras on the given graph. Returns two dicts
	equal to the ending distance vector for each node and the previous node
	in the path for each node
	"""

	#I realize this can be done faster with a heap
	q = set()

	distance = {}
	previous = {}
	for node in graph.get_nodes():
		distance[node] = math.inf
		previous[node] = None
		q.add(node)

	distance[start_node] = 0

	while len(q) > 0:
		current_node = get_min_distance_node(distance, q)
		q.remove(current_node)

		for edge in graph.get_edges(current_node):
			new_distance = distance[current_node] + edge[1]
			if new_distance < distance[edge[0]]:
				distance[edge[0]] = new_distance
				previous[edge[0]] = current_node

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
	d,p = dijkstras(g, sys.argv[2])
	print_shortest_paths(g, d, p, sys.argv[2])
	