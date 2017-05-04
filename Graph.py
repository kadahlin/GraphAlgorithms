#Kyle Dahlin

#Read from a kgraph file and return a adjancy list representation of that graph

#A kgraph file is plain text where each line is values seperated by spaces. The first value on 
# a line is the source node that this edge comes from. Everything after this is the destination 
#edge and the weight of that edge. The format must be exacly this: one source value and an even 
#number of values after that to create the graph object.

from collections import defaultdict
import sys 

class Graph:

	def get_nodes(self):
		"""
		Return a set containing all of the vertices in the graph
		"""
		keys = set()
		for key in self.graph:
			keys.add(key)
		return keys

	def get_edges(self, node):
		"""
		Return a list containing all of the edges going out of node
		"""
		return self.graph[node]

	def create_graph(self, filename):
		"""
		Create a graph that is a dict with {node: [(edges)]}
		"""
		with open(filename) as f:
			lines = f.readlines()
			for line in lines:
				values = line.split()
				node = values[0]
				edges = []
				for index in range(1, len(values[1:]), 2):
					edges.append((values[index], int(values[index+1])))
				self.graph[node] = edges

	def __init__(self, filename):
		"""Create the graph from the file at filename"""
		self.graph = defaultdict(list)
		self.create_graph(filename)

if __name__ == '__main__':
	g = Graph(sys.argv[1])
	for node in g.get_nodes():
		print("{} -> {}".format(node, g.get_edges(node)))

