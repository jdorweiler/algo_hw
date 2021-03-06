#!/usr/bin/env python2
import numpy as np 
#import matplotlib as plt
import sys
#import pylab
import re
from collections import defaultdict
import copy as copy
import math

# graph with x,y points
graph = []

# minimum spanning tree
MST = []

# dictionary of edges in form  { dist : [point1, point2]. .. }
dist = []

# disjoint sets
Sets = []

def main(argv):
    global graph, MST, dist, edge_matrix

    if len(argv) < 2:
        #print "usage: ", argv[0], " [input_file]"
        return

    total = 10000000000000
    visitedPoints = []
    getInput(argv)

    # create a list of sets
    for x in graph:
        Sets.append(set([x[0]]))

    # Generate a MST
    getMST(graph, dist, MST)

    ##print "MST: ", MST
    ##print "dist: ", dist
        ##print graph

    # Change number of iterations based on how many elements are in the MST
    max_search = 1
    '''if len(MST) < 100:
        max_search = len(MST)
    elif len(MST) < 200:
        max_search = len(MST)/4
    else:
        max_search = int(np.sqrt(len(MST)))
    '''


    for start in range(0,1):
        temp_total, temp_tour = tour(MST, dist, start)
        ##print temp_total, total
        if temp_total < total and temp_total > 0:
            total = temp_total
            visitedPoints = copy.deepcopy(temp_tour)
            #print "found shorter tour"
        #print "started at", start, ". Distance=", temp_total
        ##print "visited order:", visitedPoints

    #print "Points visited in order: ", visitedPoints
    #print "Writing output file..."

    f = open(argv[1] + ".tour", 'w')
    f.write(str(total) + '\n')
    for city in range(len(visitedPoints)-1):
        f.write(str(visitedPoints[city] + '\n'))
    f.close()
    print "Output written to:", argv[1] + ".tour"

    #print MST
    #plot(visitedPoints)

def find_element_in_list(element,list_element):
        try:
            index_element=list_element.index(element)
            return 0
        except ValueError:
            return 1

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

        ##print "==MST: ", MST

    if not len(q):
        q.append(point)

    while len(q):
        # get next point
        ##print "queue before pop: ", q
        point = q.pop()
        if visited:
            total += dist_matrix[ (visited[-1], point) ]
            #  #print "Adding segment ", (visited[-1], point)
            #  #print "==Total: ", total
        visited.append(point)
        neighbors = [] # clear neighbors here??
        #print "Visiting: ", point
        #print "Current queue: ", q
        #print "Current visited: ", visited

        # add neighbors
        for x in MST:
           # #print "x in MST: ", x
            # find all edges with this point in it
            if ((point == x[0]) or (point == x[1])):
                # add edges to neighbor list
                for i, (key, value )in enumerate(dist):
                  #  #print "key value", key, value
                    if len(set(x) & set(value)) == 2:
                        #print "Added edge", key,value, " to neighbors"
                        neighbors.append((key,value))

               # #print "===NEIGHBORS: ",sorted(neighbors)
        # push neighbors in sorted distance order to queue

        for y in reversed(sorted(neighbors)):
        ##print "Looking at edge ", y, "for point", point
        ##print "neighbor[y][0]=", neighbors[y][0]
        ##print "neighbor[y][1]=", neighbors[y][1]
            #print "checking point", point, " neighbors ", neighbors, " y ", y
            # add all unvisited neighbors to queue
            #print "checking neighbor", y[1][0]
            if (int(y[1][0]) != point):
                #print "True"
                if(find_element_in_list(y[1][0], visited)):
                    if(find_element_in_list(y[1][0], q)):
                        #print "adding [y][0]: ", y[1][0]
                        q.append(y[1][0])
            #print "checking neighbor", y[1][1]
            if (y[1][1] != point):
                #print "True"
                if(find_element_in_list(y[1][1], visited)):
                    if(find_element_in_list(y[1][1], q)):
                        #print "adding [y][1]: ", y[1][1]
                        q.append(y[1][1])
        #print "queue at end: ", q

    # add the distance from the last point to the start
    # point to the total
    total += dist_matrix[ (visited[-1], start) ]
        
    # append the start point to visited to complete the cycle
    visited.append(start)   # grader doesn't want first point put in again

    return total, visited


def getMST(graph, dist, MST):
    global total, dist_matrix 
    # calculate the distances from our start
    # to all other points in the graph
    # this is in the form { dist : [point1, point2] ... }
    # so that we can iterate through them in sorted order
    pairs = []
    dist_matrix = {}
    for point1 in graph:
        for point2 in graph:
            # add the distance from point1 to point2
            d = int(round(math.sqrt( (int(point1[1])-int(point2[1]))**2 + (int(point1[2])-int(point2[2]))**2 )))
            dist_matrix[(point1[0], point2[0])] = d
            dist_matrix[(point2[0], point1[0])] = d

            if(d > 0):
                dist.append((d,[point1[0], point2[0]]))


    # go through the list of edges in sorted order
    # check each edge using checkEdge to see if both
    # points are already in the MST
    for x in sorted(dist, key=lambda entry: entry[0]):
        ##print "x: ",x
        # exclude 0 distance:
        if x == 0:
            continue

        # mst is empty, add lowest edge
        if len(MST) == 0:
            MST.append(x[1])
            Sets[int(x[1][0])] = Sets[int(x[1][0])].union(Sets[int(x[1][1])])
            Sets.pop(int(x[1][1]))

        else:
            # see if both points are in MST already
            if(checkEdge(x[1], MST, dist)):
                ##print "Added edge: ", dist[x]
                MST.append(x[1])
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
   # #print x
    for y in MST:
        ##print "checking ", y, dist[x]
    # check to see if both points are in the MST already
    # skip this edge if they are, set a flag for each x,y val
        if ((x[0] == y[0]) or (x[0] == y[1])):
           # #print "found x"
            x_val = 1
        if ((x[1] == y[0]) or (x[1] == y[1])):
           # #print "found y"
            y_val = 1
        if (x_val and y_val):
            break
    
    # return 0 to skip this edge
    if(x_val and y_val):
        # check for disjoint sets
        for s in Sets:
            ##print s, dist[x]
            if((x[0] in s) and (x[1] in s)):
                ##print "Skipping edge: ", dist[x]
                return 0
    # union the two points
    if(findUnion(x) == 0):
        return 0

    ##print "After: ", Sets
    return 1        

def findUnion(points):
    # this check the list of sets and makes sure 
    # that the two points are not in the same set
    # already (ie creating a cycle).  If they are
    # not in the same set it joins the two sets
    ind1 = None
    ind2 = None

    ##print "Before: ", Sets
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

    ##print "Joining: ", point1, point2, ind1, ind2

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
    #print len(x_points)

    
    # this plots a scatter of the points
    for i in graph:
        #print i
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
    
    ##print graph

    plt.pyplot.show()

if __name__ == '__main__':
    main(sys.argv)
