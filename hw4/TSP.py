import numpy as np 
import matplotlib as plt
import sys
import pylab
import re

graph = []

def main(argv):
	if len(argv) < 2:
		print " ***  No input file given, exiting  ***"
		return

	getInput(argv)

	plot()


# read in the text file and tokenize into 
# a list of lists [ [node, edge1, edge2] .... ]
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
	global graph

	x_points = []
	y_points = []

	# separate x,y for plotting
	for i in range(len(graph)):
		x_points.append(int(graph[i][1]))
		y_points.append(int(graph[i][2]))

	plt.pyplot.scatter(x_points,y_points)
	plt.pyplot.show()

if __name__ == '__main__':
	main(sys.argv)
