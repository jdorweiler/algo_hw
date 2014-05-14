from pulp import *
import numpy as np
points = [[1,3], [2,5], [3,7], [5,11], [7,14], [8,15], [10,19]]

#set up variables
x = LpVariable("X_i")
y = LpVariable("Y_i")
c = LpVariable("C")

# Create the 'prob' variable to conmitain the problem data
prob = LpProblem("min max line", LpMinimize)

#objective to minimize
# minimize the sum of all the distances from a line to each point
for i in range(len(points)):
	prob += points[i][0]*x+points[i][1]*y-c

prob += x > 8
prob += y > 0
# The problem data is written to an .lp file
prob.writeLP("minmaxline.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen    
print "Total net profit  = ", value(prob.objective)
