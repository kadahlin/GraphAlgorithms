#Kyle Dahlin 

#Implementations of the Prim-Jarnik algorithm

from Graph import Graph
import math
import sys

def prims(graph: Graph, starting_node: str):
	tree = set()
	costs = {}
	min_edges = {}
	nodes = graph.get_nodes()
	for node in nodes:
		costs[node] = math.inf
	for node in nodes:
		min_edges[node] = None
	costs[starting_node] = 0

	while len(nodes) != 0:
		#Yea i know this can be faster with a heap but I was studying for a midterm when I 
		#made this, sue me
		min_node = None
		for node in nodes:
			if min_node == None:
				min_node = node
			elif costs[node] < costs[min_node]:
				min_node = node

		nodes.remove(min_node)

		if min_edges[min_node] != None:
			print("Adding {} to tree".format(min_edges[min_node]))
			tree.add(min_edges[min_node])

		for edge in graph.get_edges(min_node):
			if edge[0] in nodes and edge[1] < costs[edge[0]]:
				costs[edge[0]] = edge[1]
				min_edges[edge[0]] = edge

	return tree

if __name__ == '__main__':
	#Take a kgraph file and a starting node as parameters.
	#Kgraphs are explained in Graph.py
	g = Graph(sys.argv[1])
	mst = prims(g, sys.argv[2])
	print("{}FINAL MST{}".format('-'*6, '-'*6))
	[print(edge) for edge in mst]
