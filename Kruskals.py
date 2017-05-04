#Kyle Dahlin 

#Implementation of Kruskals algorithm

from Graph import Graph
from disjoint_set import Disjoint
import math
import sys


def kruskals(graph: Graph):
	forest = None
	for node in graph.get_nodes():
		if not forest:
			forest = Disjoint(node)
		else:
			forest.create_set(node)

	tree = []
	all_edges = []
	for node in graph.get_nodes():
		for edge in graph.get_edges(node):
			all_edges.append((node, edge[0], edge[1]))
	for edge in sorted(all_edges, key=lambda x: x[2]):
		if not forest.test_same_set(edge[0], edge[1]):
			tree.append(edge)
			forest.merge_sets(edge[0], edge[1])
		if forest.size() == 1:
			return tree

if __name__ == '__main__':
	#Take a kgraph file as a parametere
	#Kgraphs are explained in Graph.py
	g = Graph(sys.argv[1])
	mst = kruskals(g)
	print("{}FINAL MST{}".format('-'*6, '-'*6))
	[print("{}->{}({})".format(edge[0], edge[1], edge[2])) for edge in mst]