import sys
import csv
import random
import math
from numpy.random import RandomState
clusters = 80
filename = "breast-cancer-wisconsin.data.txt"
rows = sum(1 for line in open(filename))
rows = rows + 1
columns = 10
myDataset = [[0 for x in range(columns)] for y in range(rows)]
myList = []
i = 0
with open(filename, 'r') as fileObj:
	reader = csv.reader(fileObj)
	for line in reader:
		myList = line
		k = 1
		for j in range(0, columns):
			myDataset[i][j] = myList[k]
			k += 1
		i += 1
for i in range(0, columns):
	myDataset[699][i] = myDataset[0][i]
for i in range(0, columns - 1):
	for j in range(0, rows):
		if myDataset[j][i] == "?":
			if myDataset[j][columns - 1] == 2.0:
				myDataset[j][i] = 1.34
			else:
				myDataset[j][i] = 7.62
for i in range(0, rows):
	for j in range(0, columns): 
			myDataset[i][j] = float(myDataset[i][j])
for i in range(0, rows):
	temp = myDataset[i][0]
	myDataset[i][0] = myDataset[i][columns - 1]
	myDataset[i][columns - 1] = temp
for i in range(0, rows):
	if myDataset[i][0] == 2.0:
		myDataset[i][0] = 0.0
	else:
		myDataset[i][0] = 1.0	
state = RandomState()
r = random.Random()
r.seed()
for i in range(0, rows - 1):
	randRow = state.randint(i, rows - 1)
	for j in range(0, columns):
		temp = myDataset[i][j]
		myDataset[i][j] = myDataset[randRow][j]
		myDataset[randRow][j] = temp
count = truePos = falsePos = trueNeg = falseNeg = 0
total = 0
for iteration in range(0, 10):
	trainRows = (rows / 10) * 9
	testRows = (rows / 10)
	trainSet = [[0 for x in range(columns)] for y in range(trainRows)]
	testSet = [[0 for x in range(columns)] for y in range(testRows)]
	offset = iteration * testRows
	offList = []
	for i in range(0, testRows):
		for j in range(0, columns):
			testSet[i][j] = myDataset[offset + i][j]
		offList.append(offset + i)
	index = -1
	for i in range(0, rows):
		if i not in offList:
			index += 1
			for j in range(0, columns):
				trainSet[index][j] = myDataset[i][j]
	clist = []
	for k in range(0, clusters):
		while 1:
			randRow = state.randint(0, trainRows - 1)
			if randRow not in clist:	
				clist.append(randRow)
				break
	clusterSet = [[0 for x in range(columns)] for y in range(clusters)]
	for i in range(0, clusters):
		for j in range(0, columns):
			clusterSet[i][j] = trainSet[clist[i]][j]
	clusterMem = [-1 for x in range(trainRows)]
	clusterMem2 = [-1 for x in range(trainRows)]
	while 1:
		for i in range(0, trainRows):
			minDist = sys.maxint
			for j in range(0, clusters):
				dist = 0
				for k in range(1, columns):
					dist += (trainSet[i][k] - clusterSet[j][k]) * (trainSet[i][k] - clusterSet[j][k]) 
				dist = math.sqrt(dist)
				if dist <= minDist:
					minDist = dist
					clusterMem[i] = j
		flag = 0
		for i in range(0, trainRows):
			if clusterMem[i] != clusterMem2[i]:
				flag = 1
				break
		if flag == 0:
			average = 0
			for c in range(0, clusters):
				distance = 0
				ctr = 0
				for r in range(0, trainRows):
					if clusterMem[r] == c:
						distance2 = 0
						ctr += 1
						for s in range(1, columns):
							distance2 += (trainSet[r][s] - clusterSet[c][s]) ** 2
						distance += math.sqrt(distance2)
				if ctr == 0:
					average = average + 0
				else:
					average += distance / ctr
			average = average/clusters
			total = float(total) + average
			break
		for i in range(0, trainRows):
			clusterMem2[i] = clusterMem[i]
		for i in range(0, clusters):
			for j in range(1, columns):
				distSum = 0
				ctr = 0
				for k in range(0, trainRows):
					if clusterMem[k] == i:
						distSum += trainSet[k][j]
						ctr += 1
				if ctr != 0:
					clusterSet[i][j] = float(distSum) / float(ctr)
			class_0 = class_1 = 0
			for k in range(0, trainRows):
				if clusterMem[k] == i:
					if trainSet[k][0] == 0.0:
						class_0 += 1
					else:
						class_1 += 1
			if class_0 > class_1:
				clusterSet[i][0] = 0
			else:
				clusterSet[i][0] = 1
	for i in range(0, testRows):
		minDist = sys.maxint
		for j in range(0, clusters):
			dist = 0
			for k in range(1, columns):
				dist += (testSet[i][k] - clusterSet[j][k]) * (testSet[i][k] - clusterSet[j][k])
			dist = math.sqrt(dist)
			if dist <= minDist:
				minDist = dist
				clusterMember = j
		predicted = clusterSet[clusterMember][0]
		if predicted == 0.0 and testSet[i][0] == 0.0:
			count += 1
			trueNeg += 1
		elif testSet[i][0] == 1.0 and predicted == 0.0:
			falseNeg += 1
		elif testSet[i][0] == 1.0 and predicted == 1.0:
			truePos += 1
			count += 1
		else:
			falsePos += 1
accuracy = float(count) / float(rows)
print "\n"
print "Accuracy : ", accuracy,"\n"
print "n  = ",rows,"\t","Predicted No","\t","Predicted Yes"
print "Actual No\t   ", trueNeg,"\t   ", falsePos
print "Actual Yes\t   ", falseNeg,"\t\t   ", truePos
print "Precision\t", float(truePos) / float(truePos + falsePos)
print "Recall\t\t", float(truePos) / float(truePos + falseNeg)
print float(total)/10
del myDataset