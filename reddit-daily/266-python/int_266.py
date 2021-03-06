# Reddit Daily Programmer #266 [Intermediate] - Graph Radius and Diameter
# https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/

# Note: Each solution function for this challenge requires an adjacency matrix A as input

import easy_266 as easy
import math


def ecc(A, v):
	# Use Dijkstra's algorithm to determine shortest distances
	# between node 'v' and all other nodes, then find the max
	
	# Distance and visitation arrays
	N = len(A)
	dist = [math.inf]*N
	visited = []
	
	# Initial distance
	dist[v-1] = 0
	
	# Dijkstra's algorithm
	while len(visited) != N:
		# Grab the next node to visit by:
		#  1. Create a sub-list of distances of unvisited nodes
		#  2. Find the minimum distance from this reduced set
		d, node = min((dist[i], i) for i in range(N) if i not in visited)
		
		# Add node to visited node set
		visited.append(node)
		
		# Update all neighbors of the current node with new distances
		for i in range(N):
			if A[node][i] and ((dist[node]+1) < dist[i]):
				dist[i] = dist[node] + 1
	
	return max(i for i in dist if i is not math.inf)


def eccAll(A):
	ex = []
	for i in range(1, len(A)+1):
		ex.append(ecc(A, i))
	
	return ex


def rad(A):
	ex = eccAll(A)
	return min(i for i in ex if i > 0)


def diam(A):
	ex = eccAll(A)
	return max(ex)


def center(A):
	# Unverified function -- written for the description of the challenge
	# but its operation and results are untested
	
	r = rad(A)
	ex = eccAll(A)
	
	v = []
	for i in range(len(ex)):
		if ex[i] == r:
			v.append(i+1)
	
	return v


# Helper function
def compressID(edges):
	# This function takes a list of tuples (representing edges) where
	# each node has a unique string or numeric ID, and maps the IDs
	# to a unique number 1..N. The input list will be modified according
	# to the mapping.
	nodes = {}
	for E in edges:
		nodes[E[0]] = 1
		nodes[E[1]] = 1
	
	# Create 1-to-1 mapping for current IDs to sequential IDs
	index = 1
	for key, val in sorted(nodes.items()):
		nodes[key] = index
		index += 1
	
	# Map current IDs to new IDs
	for itr in range(len(edges)):
		edges[itr] = (nodes[edges[itr][0]], nodes[edges[itr][1]])
	
	# Return mapping (edges argument is passed by reference)
	return nodes


def test(filename):
	# The file format is slightly different for this challenge and IDs
	# are non-sequential
	num_edges, edges = easy.load(filename)
	mapping = compressID(edges)
	num_nodes = len(mapping)
	
	adj = easy.adjacency(num_nodes, edges, True)
	
	print("Radius:", rad(adj))
	print("Diameter:", diam(adj))
