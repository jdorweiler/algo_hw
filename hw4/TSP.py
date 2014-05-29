#!/usr/bin/env python2

import numpy as np 
import matplotlib as plt
import sys
import pylab
import re
from collections import deque

# graph with x,y points
graph = []

# minimum spanning tree
MST = []

# dictionary of edges in form  { dist : [point1, point2]. .. }
dist = {}

# disjoint sets
Sets = []

def main(argv):
	global graph, MST, dist

	if len(argv) < 2:
		print "usage: ", argv[0], " [input_file]"
		return

	total = 10000000000000
	visitedPoints = []
	getInput(argv)

	# create a list of sets
	for x in graph:
		Sets.append(set({x[0]}))

	# Generate a MST
	getMST(graph, dist, MST)

	print "MST: ", MST

	# Change number of iterations based on how many elements are in the MST
	max_search = 1
	if len(MST) < 100:
		max_search = len(MST)
	elif len(MST) < 200:
		max_search = len(MST)/4
	else:
		max_search = int(np.sqrt(len(MST)))


	for start in range(0,max_search):
		temp_total, temp_tour = tour(MST, dist, start)
		#print temp_total, total
		if temp_total < total and temp_total > 0:
			total = temp_total
			visitedPoints = temp_tour
		print "started at", start, ". Distance=", temp_total

	print "Points visited in order: ", visitedPoints
	print "Total distance: ", total
	print "Writing output file..."

	f = open(argv[1] + ".tour", 'w')
	f.write(str(total) + '\n')
	for city in visitedPoints:
		f.write(str(city) + '\n')
	f.close()
	print "Output written to:", argv[0] + ".tour"
	
	#plot(visitedPoints)



def tour(MST, dist, startPoint):
	# MST is a list of edges that are included in our 
	# minimum spanning tree.  
	# Pick an edge from the MST, then choose one of the points
	# in that edge as our starting point,  Look up the distances
	# from that point to its neighbors (dist has these values)
	# and push its neighbor points to a priority queue (BFS)
	# add the current point to the list of visited points
	# and repeat
	total = 0

	##q = deque() # our priority queue

	visited = [] # list of visited points
	point = str(startPoint) # pick first point for now, try random later
	start = point
	q = [start]    # using a stack for DFS for pre-order walk
	#neighbors = {}

	if not len(q):
		q.append(point)

	while len(q):
		# get next point
		#print "queue before pop: ", q
		point = q.pop()
		visited.append(point)
		neighbors = {} # clear neighbors here??
		#print "Visiting: ", point

		# add neighbors
		for x in MST:
			# find all edges with this point in it
			if point == x[0] or point == x[1]:
				# add edges to neighbor list
				for key, value in dist.items():
					if x == value:
						neighbors[key] = value

		# push neighbors in sorted distance order to queue
		for y in reversed(sorted(neighbors)):
			#print y
			if neighbors[y][0] != point:
				if neighbors[y][0] not in visited:
					#print "adding: ", neighbors[y][0]
					q.append(neighbors[y][0])

			elif neighbors[y][1] != point:
				if neighbors[y][1] not in visited:
					#print "adding: ", neighbors[y][1]
					q.append(neighbors[y][1])
					total += y

	# add the distance from the last point to the start
	# point to the total
	for y in dist:
		if dist[y][0] == start and dist[y][1] == point:
			total += y
			break
		if dist[y][1] == start and dist[y][0] == point:
			total += y
			break
		
	# append the start point to visited to complete the cycle
	visited.append(start)
	return total, visited

def getMST(graph, dist, MST):
	global total
	# calculate the distances from our start
	# to all other points in the graph
	# this is in the form { dist : [point1, point2] ... }
	# so that we can iterate through them in sorted order
	for point1 in graph:
		for point2 in graph:
			# add the distance from point1 to point2
			dist[int(np.sqrt( (int(point1[1])-int(point2[1]))**2 + (int(point1[2])-int(point2[2]))**2 ))] = [point1[0], point2[0]]

	# go through the list of edges in sorted order
	# check each edge using checkEdge to see if both
	# points are already in the MST
	for x in sorted(dist):
		# exclude 0 distance:
		if x == 0:
			continue

		# mst is empty, add lowest edge
		if len(MST) == 0:
			MST.append(dist[x])
			Sets[int(dist[x][0])] = Sets[int(dist[x][0])].union(Sets[int(dist[x][1])])
			Sets.pop(int(dist[x][1]))
		else:
			# see if both points are in MST already
			if(checkEdge(x, MST, dist)):
				#print "Added edge: ", dist[x]
				MST.append(dist[x])
				#plot()

		if(len(Sets) == 1):
			return
		
def checkEdge(x, MST, dist):
	# check to see if both points are in the MST already
	# if this is true then check to see if the points
	# are part of the same set. If they are two 
	# different sets then we add the edge to the MST
	y_val = 0
	x_val = 0

	for y in MST:
	# check to see if both points are in the MST already
	# skip this edge if they are, set a flag for each x,y val
		if ((dist[x][0] == y[0]) or (dist[x][0] == y[0])):
			x_val = 1
		if ((dist[x][1] == y[0]) or (dist[x][0] == y[0])):
			y_val = 1
	
	# return 0 to skip this edge
	if(x_val and y_val):
		# check for disjoint sets
		for s in Sets:
			if((dist[x][0] in s) and (dist[x][1] in s)):
				#print "Skipping edge: ", dist[x]
				return 0
	# union the two points
	if(findUnion(dist[x]) == 0):
		return 0

	#print "After: ", Sets
	return 1		

def findUnion(points):
	# this check the list of sets and makes sure 
	# that the two points are not in the same set
	# already (ie creating a cycle).  If they are
	# not in the same set it joins the two sets
	ind1 = None
	ind2 = None

	#print "Before: ", Sets
	for index, s in enumerate(Sets):
		if(points[0] in s):
			point1 = s
			ind1 = index
		if(points[1] in s):
			point2 = s
			ind2 = index

		# both in the same set, return 0 to skip
		if((ind1 == ind2) and (ind1 is not None)):
			return 0

	#print "Joining: ", point1, point2, ind1, ind2

	# join the two sets
	Sets[ind1] = Sets[ind1].union(Sets[ind2])

	# remove the extra one from the list
	Sets.pop(ind2)

def getInput(argv):
	# read in the text file and tokenize into 
	# a list of lists [ [node, point1, point2] .... ]
	global graph

	with open(argv[1]) as file:
		graph = file.readlines()

	file.close()

	graph = [x.strip('\n\r ') for x in graph] 

	# remove multiple spaces
	graph = [re.sub("\s\s+" , " ", x) for x in graph]

	# split into numbers on a space
	graph = [x.split(' ') for x in graph] 

def plot(visited):
	global graph, MST

	x_points = []
	y_points = []

	fig, ax = plt.pyplot.subplots()
	'''
	# this plots the MST
	# separate x,y for plotting
	for i in MST:
		x_points.append(int(graph[int(i[0])][1]))
		y_points.append(int(graph[int(i[0])][2]))
		ax.annotate(i[0],
			xytext=(-5,5), 
			textcoords='offset points', 
			xy=( x_points[len(x_points)-1], 
				y_points[len(y_points)-1]) )

		plt.pyplot.scatter( x_points[len(x_points)-1], y_points[len(y_points)-1])

		x_points.append(int(graph[int(i[1])][1]))
		y_points.append(int(graph[int(i[1])][2]))
		ax.annotate(i[1],
			xytext=(-5,5), 
			textcoords='offset points', 
			xy=( x_points[len(x_points)-1], 
				y_points[len(y_points)-1]) )

		plt.pyplot.scatter( x_points[len(x_points)-1], y_points[len(y_points)-1])

		plt.pyplot.plot(x_points[len(x_points)-2: ], y_points[len(y_points)-2:] )
	'''	

	'''
	# this plots a scatter of the points
	for i in graph:
		print i
		x_points.append(int(i[1]))
		y_points.append(int(i[2]))
	
	'''

	for i in visited:
		x_points.append(int(graph[int(i)][1]))
		y_points.append(int(graph[int(i)][2]))
		ax.annotate(i,
			xytext=(-5,5), 
			textcoords='offset points', 
			xy=( x_points[len(x_points)-1], 
				y_points[len(y_points)-1]) )

		plt.pyplot.scatter( x_points[len(x_points)-1], y_points[len(y_points)-1])

	plt.pyplot.plot(x_points, y_points)
	#print graph

	plt.pyplot.show()

if __name__ == '__main__':
	main(sys.argv)
