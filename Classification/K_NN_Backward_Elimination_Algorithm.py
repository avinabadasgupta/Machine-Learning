import csv
import random
import math
from numpy.random import RandomState
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
				myDataset[j][i] = 1
			else:
				myDataset[j][i] = 8
for i in range(0, rows):
	for j in range(0, columns): 
			myDataset[i][j] = float(myDataset[i][j])
for i in range(0, rows):
	temp = myDataset[i][0]
	myDataset[i][0] = myDataset[i][columns - 1]
	myDataset[i][columns - 1] = temp
for i in range(0, rows):
	for j in range(1, columns):
		myDataset[i][j] = myDataset[i][j] / (1 + myDataset[i][j])
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
trainRows = (rows / 10) * 9
testRows = (rows / 10)
trainSet = [[0 for x in range(columns)] for y in range(trainRows)]
testSet = [[0 for x in range(columns)] for y in range(testRows)]
offset = 0 * testRows
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
count = truePos = falsePos = trueNeg = falseNeg = 0
for i in range(0, trainRows):
	distance = {}
	for j in range(0, trainRows):
		if j != i:
			dist = 0
			for k in range(1, columns):
				dist += (trainSet[i][k] - trainSet[j][k]) * (trainSet[i][k] - trainSet[j][k])
			dist = math.sqrt(dist)
			if dist not in distance.keys():
				distance[dist] = [trainSet[j][0]]
			else:
				distance[dist].append(trainSet[j][0])
	keylist = distance.keys()
	keylist.sort()
	class_0 = class_1 = 0
	knn = 5
	k = dCount = 0
	while dCount <= knn:
		for d in range(0, len(distance[keylist[k]])):
			if distance[keylist[k]][d] == 0.0:
				class_0 += 1
			else:
				class_1 += 1
			dCount += 1
			if dCount > knn:
				break
		k += 1
	if class_0 > class_1:
		predicted = 0.0
	else:
		predicted = 1.1
	if predicted == trainSet[i][0]:
		count += 1
accuracy = float(count) / float(trainRows)
accuracy_2 = accuracy
removeList = []
for rCol in range(1, columns):
	count = 0
	for i in range(0, trainRows):
		distance = {}
		for j in range(0, trainRows):
			if j != i:
				dist = 0
				for k in range(1, columns):
					if k != rCol:
						if k not in removeList:
							dist += (trainSet[i][k] - trainSet[j][k]) * (trainSet[i][k] - trainSet[j][k])
				dist = math.sqrt(dist)
				if dist not in distance.keys():
					distance[dist] = [trainSet[j][0]]
				else:
					distance[dist].append(trainSet[j][0])
		keylist = distance.keys()
		keylist.sort()
		class_0 = class_1 = 0
		knn = 5
		k = dCount = 0
		while dCount <= knn:
			for d in range(0, len(distance[keylist[k]])):
				if distance[keylist[k]][d] == 0.0:
					class_0 += 1
				else:
					class_1 += 1
				dCount += 1
				if dCount > knn:
					break
			k += 1
		if class_0 > class_1:
			predicted = 0.0
		else:
			predicted = 1.1
		if predicted == trainSet[i][0]:
			count += 1
	accuracy = float(count) / float(trainRows)
	if accuracy > accuracy_2:
		removeList.append(rCol)
		accuracy_2 = accuracy
count = 0
for i in range(0, testRows):
		distance = {}
		for j in range(0, trainRows):
			dist = 0
			for k  in range(1, columns):
				if k not in removeList:
					dist += (trainSet[j][k] - testSet[i][k]) * (trainSet[j][k] - testSet[i][k]) 
			dist = math.sqrt(dist)
			if dist not in distance.keys():
				distance[dist] = [trainSet[j][0]]
			else:
				distance[dist].append(trainSet[j][0])
		keylist = distance.keys()
		keylist.sort()
		class_0 = class_1 = 0
		knn = 5
		k = dCount = 0
		while dCount <= knn:
			for d in range(0, len(distance[keylist[k]])):
				if distance[keylist[k]][d] == 0.0:
					class_0 += 1
				else:
					class_1 += 1
				dCount += 1
				if dCount > knn:
					break
			k += 1
		if class_0 > class_1:
			predicted = 0.0
		else:
			predicted = 1.1
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
print "n  = ",rows/10,"\t","Predicted No","\t","Predicted Yes"
print "Actual No\t   ", trueNeg,"\t   ", falsePos
print "Actual Yes\t   ", falseNeg,"\t\t   ", truePos
if truePos == 0:
	print "Precision\t", 0
else:
	print "Precision\t", float(truePos) / float(truePos + falsePos)
if truePos == 0:
	print "Recall\t\t", 0
else: 
	print "Recall\t\t", float(truePos) / float(truePos + falseNeg)
del myDataset
