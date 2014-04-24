import numpy as np 
import time
from matplotlib import pyplot as plt 

stepSize = 100

def main():

	#three maps to hold runtimes for each algo
	rt1 = []
	rt2 = []
	rt3 = []

	# test each algo 2 times to average results
	for i in range(2):
		
		for n in range(0,1000,100):
			#generte a random array
			testArr = np.random.random_integers(100, size=(n,))-50

			# test algo1
			#algo1 takes a stupid amount of time to run so limit to 900
			if(n < 901):
				start = time.time()
				algo1(testArr)
				stop = time.time()
				addToList(rt1, (stop-start), n, i, 100)

			#test algo2
			start = time.time()
			algo2(testArr)
			stop = time.time()
			addToList(rt2, (stop-start), n, i, 100)

			#test algo3		
			start = time.time()
			print "Algo3: ", algo3(testArr)
			stop = time.time()
			addToList(rt3, (stop-start), n, i, 100)

	makePlot(rt1, rt2, rt3, 900)
#	makePlot(rt1, rt2, rt3, 9000)

def addToList(array, value, n, i,stepSize):
	index = n/stepSize
	# when running several times to get averages..
	# first time through we need to append to the list
	# each time after that we calculate the average
	if(i):
		array[index][1] = (array[index][1] + value) / 2
	else:
		array.append( [n, value] )

def algo1(array):
	maxSum = -99999
	if len(array) == 1:
		maxSum = array[0]
	else:
		for e in range(len(array)):
			for j in range(e,len(array)):
				maxSum = np.maximum(maxSum, sum(array[e:j]))
	print "Algo1: ",maxSum

def algo2(array):
	maxSum = -99999
	for e in range(len(array)):
		testSum = 0
		for j in range(e,len(array)):
			testSum += array[j]
			maxSum = np.maximum(maxSum, testSum)
	print "Algo2: ",maxSum

#this still needs work
def algo3(array):
	if(len(array) == 0):
		return 0
	if(len(array) == 1):
		return array[0]

	mid = len(array)/2
	tempL = tempR = 0
	maxLeft = maxRight = -99999

	#left side crossing -- mid backwards
	for i in range(mid,0,-1):
		tempL = tempL + array[i]
		maxLeft = np.maximum(maxLeft, tempL)

	#right side crossing -- mid forwards
	for j in range(mid+1, len(array)):
		tempR = tempR + array[j]
		maxRight = np.maximum(maxRight, tempR)
	maxCrossing = maxLeft + maxRight

	MaxA = algo3(array[:mid])
	MaxB = algo3(array[mid+1:])

	return np.maximum(np.maximum(MaxA, MaxB),maxCrossing)


def makePlot(data1, data2, data3, limit):
	data1 = np.array(data1)
	data2 = np.array(data2)
	data3 = np.array(data3)

	# make plots
	plt.subplot(2,1,1)


	x = data1[:,0]
	y = data1[:,1]
	plt.plot(x[1:limit],y[1:limit], label="n^3 Algorithm")


	x2 = data2[:,0]
	y2 = data2[:,1]
	plt.plot(x2[1:limit],y2[1:limit], label="n^2 Algorithm")

	x3 = data3[:,0]
	y3 = data3[:,1]
	plt.plot(x3[1:limit],y3[1:limit], label="nLogN Algorithm")

	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel("Array Size", labelpad=-5)
	plt.ylabel("Run time (s)")
	plt.legend(loc='upper center', bbox_to_anchor=(0.15,1), prop={'size':8})

	plt.subplot(2,1,2)

	x = data1[:,0]
	y = data1[:,1]
	plt.plot(x,y, label="n^3 Algorithm")


	x2 = data2[:,0]
	y2 = data2[:,1]
	plt.plot(x2,y2, label="n^2 Algorithm")

	x3 = data3[:,0]
	y3 = data3[:,1]
	plt.plot(x3,y3, label="nLogN Algorithm")

	algo1Fit = np.poly1d(np.polyfit(x,y,3))
	#plt.xscale('log')
	#plt.yscale('log')
	plt.xlabel("Array Size")
	plt.ylabel("Run time (s)")
	plt.show()

if __name__ == '__main__':
	main()
