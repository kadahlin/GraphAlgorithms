#Kyle Dahlin 

#Implementations of Baruvkas algorithm

#Note that when given an undirected graph it will print some duplicate edges
#	i.e. if there is an edge e <-> f that is in the MST it will print both e -> f
#	and f -> e as output. You may sort out if you like but for my understanding of the algorithm
# 	the duplicates were sufficient

from Graph import Graph
from disjoint_set import Disjoint
import math
import sys

def baruvkas(graph: Graph):
	forest = None
	for node in graph.get_nodes():
		if not forest:
			forest = Disjoint(node)
		else:
			forest.create_set(node)
	tree = []
	#Edges will be stored as (source, dest, cost)
	while forest.size() > 1:
		
		for component in forest.sets:
			edges = set()
			for node in component:
				cheapest_edge = None
				cheapest_cost = math.inf

				for edge in graph.get_edges(node):
					if edge[0] not in component and edge[1] < cheapest_cost:
						cheapest_edge = edge
						cheapest_cost = edge[1]
				if cheapest_edge != None:
					edges.add((node, cheapest_edge[0], cheapest_edge[1]))
			tree.append(min(edges, key=lambda x: x[2]))

			print("ending edges for component{} is:\n{}".format(component, edges))
		for edge in tree:
			forest.merge_sets(edge[0], edge[1])

	return tree

if __name__ == '__main__':
	#Take a kgraph file as a parametere
	#Kgraphs are explained in Graph.py
	g = Graph(sys.argv[1])
	mst = baruvkas(g)
	print("{}FINAL MST{}".format('-'*6, '-'*6))
	[print("{}->{}({})".format(edge[0], edge[1], edge[2])) for edge in mst]