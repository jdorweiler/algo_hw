from pulp import *

#set up variables, minimum of 0 for each
HAM_FRESH = LpVariable("ham fresh", 0)
HAM_SRT = LpVariable("Ham Smoked RT", )
HAM_SOT = LpVariable("Ham Smoked OT", 0)

PORK_FRESH = LpVariable("PORK fresh", 0)
PORK_SRT = LpVariable("PORK Smoked RT", 0)
PORK_SOT = LpVariable("PORK Smoked OT", 0)

P_HAM_FRESH = LpVariable("P-ham fresh", 0)
P_HAM_SRT = LpVariable("P-Ham Smoked RT", 0)
P_HAM_SOT = LpVariable("P-Ham Smoked OT", 0)


# Create the 'prob' variable to contain the problem data
prob = LpProblem("Pork Profit", LpMaximize)

# objective to solve
prob += HAM_FRESH*8+HAM_SRT*14+HAM_SOT*11+PORK_FRESH*4+PORK_SRT*12+PORK_SOT*7+P_HAM_FRESH*4+P_HAM_SRT*13+P_HAM_SOT*9

# constraints
prob += HAM_FRESH+HAM_SRT+HAM_SOT <= 480 # at most 480 ham
prob += PORK_FRESH+PORK_SRT+PORK_SOT >= 400 # at most 400 pork
prob += P_HAM_FRESH+P_HAM_SRT+P_HAM_SOT <= 230 # at most 230 picnic ham
prob += HAM_SRT+PORK_SRT+P_HAM_SRT <= 420 # max 420 smoked on RT
prob += HAM_SOT+PORK_SOT+P_HAM_SOT <= 250 # max 250 smoked on OT

# The problem data is written to an .lp file
prob.writeLP("porkprofit.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen    
print "Total net profit  = ", value(prob.objective)