import numpy as np 
import time
from matplotlib import pyplot as plt 

def main():

	rt3 = []
	rt4 = []

	# test each algo 2 times to average results
	for i in range(1):
		
		for n in range(1,500000,100000):
			#generte a random array
			testArr = np.random.random_integers(100, size=(n,))-50

			#test algo3		
			start = time.time()
			print "Algo3: ", algo3(testArr)
			stop = time.time()
			addToList(rt3, (stop-start), n, i, 100000)

			#test algo4		
			start = time.time()
			print "Algo4 ", algo4(testArr)
			stop = time.time()
			addToList(rt4, (stop-start), n, i, 100000)

	makePlot(rt3, rt4, 500000)

def addToList(array, value, n, i,stepSize):
	index = n/stepSize
	# when running several times to get averages..
	# first time through we need to append to the list
	# each time after that we calculate the average
	if(i):
		array[index][1] = (array[index][1] + value) / 2
	else:
		array.append( [n, value] )

def algo4(array):
    maxSum = -99999
    tempSum = 0
    for i in array:
    	if tempSum > 0:
    		tempSum = tempSum + i
    	else:
    		tempSum = i
    	maxSum = np.maximum(maxSum, tempSum)
    return maxSum	

#this still needs work
def algo3(array):
	if(len(array) == 0):        #O(1) for whole block
		return 0
	if(len(array) == 1):
		return array[0]

	mid = len(array)/2          # O(1) for whole block
	tempL = tempR = 0
	maxLeft = maxRight = -99999

	#left side crossing -- mid backwards
	for i in range(mid,-1,-1):  # O(n)
		tempL = tempL + array[i]    # O(1)
		maxLeft = np.maximum(maxLeft, tempL)    # O(1)

	#right side crossing -- mid forwards
	for j in range(mid+1, len(array)):  # O(n)
		tempR = tempR + array[j]    # O(1)
		maxRight = np.maximum(maxRight, tempR)  # O(1)
	maxCrossing = max(maxLeft + maxRight,maxLeft)   # O(1)

	MaxA = algo3(array[:mid])   # O(n/2)
	MaxB = algo3(array[mid:])   # O(n/2)

	return max(MaxA, MaxB, maxCrossing)
        ### Total asymptotic running time: O(n log n)


def makePlot(data1, data2, limit):
	data1 = np.array(data1)
	data2 = np.array(data2)

	# make plots
	plt.subplot(2,1,1)


	x = data1[:,0]
	y = data1[:,1]
	plt.plot(x[1:limit],y[1:limit], label="Algo 3")


	x2 = data2[:,0]
	y2 = data2[:,1]
	plt.plot(x2[1:limit],y2[1:limit], label="Algo 4 -dynamic")

	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel("Array Size", labelpad=-5)
	plt.ylabel("Run time (s)")
	plt.legend(loc='upper center', bbox_to_anchor=(0.15,1), prop={'size':8})

	plt.subplot(2,1,2)

	x = data1[:,0]
	y = data1[:,1]
	plt.plot(x,y, label="Algo 3")


	x2 = data2[:,0]
	y2 = data2[:,1]
	plt.plot(x2,y2, label="Algo 4 -dynamic")


	#plt.xscale('log')
	#plt.yscale('log')
	plt.xlabel("Array Size")
	plt.ylabel("Run time (s)")
	plt.show()

if __name__ == '__main__':
	main()
