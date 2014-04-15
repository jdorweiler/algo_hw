import numpy as np 
import time
from matplotlib import pyplot as plt 

def main():
	#three maps to hold runtimes for each algo
	rt1 = []
	rt2 = []
	rt3 = []

	for i in range(1):
		#algo1 takes a stupid amount of time to run so limit to 900
		for n in range(1,900,50):
			#generte a random array
			testArr = np.random.random_integers(100, size=(n,))-50

			# test algo1
			start = time.time()
			algo1(testArr)
			stop = time.time()
			rt1.append( [n, (stop-start)] )

			#test algo2
			start = time.time()
			algo2(testArr)
			stop = time.time()
			rt2.append( [n, (stop-start)] )

			#test algo3		
			start = time.time()
			print "Algo3: ", algo3(testArr)
			stop = time.time()
			rt3.append( [n, (stop-start)] )


	makePlot(rt1, rt2, rt3)

def algo1(array):
	maxSum = 0
	for e in range(len(array)):
		for j in range(e,len(array)):
			maxSum = np.maximum(maxSum, sum(array[e:j]))
	print "Algo1: ",maxSum

def algo2(array):
	maxSum = 0
	for e in range(len(array)):
		testSum = 0
		for j in range(e,len(array)):
			testSum += array[j]
			maxSum = np.maximum(maxSum, testSum)
	print "Algo2: ",maxSum

#this still needs work
def algo3(array):
	maxLeft = 0
	maxRight = 0
	if(len(array) == 0):
		return 0
	if(len(array) == 1):
		return array[0]

	mid = len(array)/2
	tempL = tempR = 0
	#left side
	for i in range(0,mid):
		tempL = tempL + array[i]
		maxLeft = np.maximum(maxLeft, tempL)

	#right side
	for j in range(mid,len(array)):
		tempR = tempR + array[j]
		maxRight = np.maximum(maxRight, tempR)
	maxCrossing = maxLeft + maxRight
	MaxA = algo3(array[:mid])
	MaxB = algo3(array[mid:])
	return np.maximum(np.maximum(MaxA, MaxB),maxCrossing)


def makePlot(data1, data2, data3):
	data1 = np.array(data1)
	data2 = np.array(data2)
	data3 = np.array(data3)

	# make plots
	plt.subplot(1,1,1)
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
	plt.plot(x,algo1Fit(x),'.', label="algo1 fit")

	#plt.xscale('log')
	plt.yscale('log')
	plt.xlabel("Array Size")
	plt.ylabel("Run time (s)")
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main()