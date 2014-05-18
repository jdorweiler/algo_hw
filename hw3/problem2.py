from pulp import *
import numpy as np
import matplotlib as plt
import pylab

#set up variables
x = LpVariable("X_i")
y = LpVariable("Y_i")
c = LpVariable("C")
error = LpVariable("Error")


def main():

	global x, y, c

	points = [[1,3], [2,5], [3,7], [5,11], [7,14], [8,15], [10,19]]

	# Create the 'prob' variable to conmitain the problem data
	prob = LpProblem("min max line", LpMinimize)

	#objective to minimize
	prob += error

	# add constraints
	for i in range(len(points)):
		prob += error >= points[i][1] - (points[i][0] * x +c)
		prob += error >= -points[i][1] + (points[i][0] * x +c)
	
	# The problem data is written to an .lp file
	prob.writeLP("minmaxline.lp")

	# The problem is solved using PuLP's choice of Solver
	prob.solve()

	# The status of the solution is printed to the screen
	print "Status:", LpStatus[prob.status]

	# Each of the variables is printed with it's resolved optimum value
	for v in prob.variables():
	    print v.name, "=", v.varValue

	plot(points, prob.variables())

def plot(points, variables):

	global x,y,c

	x_points = []
	y_points = []

	# separate x,y for plotting
	for i in range(len(points)):
		x_points.append(points[i][0])
		y_points.append(points[i][1])

	t = np.arange(0.0, 15.0, 1)

	line = x.varValue*t+c.varValue

	plt.pyplot.scatter(x_points,y_points)
	plt.pyplot.plot(line, 'r--');
	plt.pyplot.show()

if __name__ == '__main__':
	main()
