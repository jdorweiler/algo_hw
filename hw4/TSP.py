import numpy as np 
import matplotlib as plt
import sys
import pylab
import re

# graph with x,y points
graph = []

# minimum spanning tree
MST = []

# distance matrix
dist = {}

def main(argv):
	global graph, MST, dist

	if len(argv) < 2:
		print " ***  No input file given, exiting  ***"
		return

	getInput(argv)

	# Generate a MST
	getMST(graph, dist, MST)

	print MST

	# TODO: tour of mst to get solution

	plot()


def getMST(graph, dist, MST):
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
			#print "Adding edge: ", dist[x]
		else:
			# see if both points are in MST already
			if(checkEdge(x, MST, dist)):
				#print "Adding edge: ", dist[x]
				MST.append(dist[x])
		
def checkEdge(x, MST, dist):
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
		#print "Skipping edge: ", dist[x]
		return 0

	return 1		
		


# read in the text file and tokenize into 
# a list of lists [ [node, point1, point2] .... ]
def getInput(argv):
	global graph

	with open(argv[1]) as file:
		graph = file.readlines()

	file.close()

	graph = [x.strip('\n\r ') for x in graph] 

	# remove multiple spaces
	graph = [re.sub("\s\s+" , " ", x) for x in graph]

	# split into numbers on a space
	graph = [x.split(' ') for x in graph] 



def plot():
	global graph, MST

	x_points = []
	y_points = []

	fig, ax = plt.pyplot.subplots()

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
	# this plots a scatter of the points
	for i in graph:
		print i
		x_points.append(int(i[1]))
		y_points.append(int(i[2]))
	
	'''
	print x_points


	plt.pyplot.show()

if __name__ == '__main__':
	main(sys.argv)
