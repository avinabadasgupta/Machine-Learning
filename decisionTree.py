#Applied Machine Learning - B659
#Programming Assignment 1
#Developed and submitted by Avinaba Dasgupta and Kuntal Maiti
#Code for implementing Decision Tree
#Version 1.0
import math
import csv
import random
#definition of node class
class node:
	def __init__(self):
		#column number of node
		self.value   			= None
		#parent column number of node
		self.parent  			= None
		#each node has maximum 4 children nodes
		self.attVal1 			= None
		self.attVal2 			= None
		self.attVal3 			= None
		self.attVal4 			= None
		#entropy of node
		self.entropy    		= None
		#value of connecting branch of parent and child
		self.branchFromParent 	= None
	#method to create the decision stump or root node of decision tree	
	def insertDecisionStump(self, data):
		self.value = data
		self.entropy = entropyTarget
		currentDepth = 1
		#checks number of branches that will appear from self node
		if numOfClasses == 2:
			#create child node from branch 1
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			#if input depth is 1, stop growing and make it leaf with majority class
			if depth == 1: 
				self.attVal1.value = MajorityClass[0]
			else: 
				#if child node is not pure
				if IsPure[0] != 1:
					self.attVal1.buildTree(currentDepth + 1)
				else:
				#if child node is pure, stop growing and make it leaf with pure class	
					self.attVal1.value = MajorityClass[0]
			#create child node from branch 2
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			#if input depth is 1, stop growing and make it leaf with majority class
			if depth == 1: 
				self.attVal2.value = MajorityClass[1]
			else:
				#if child node is not pure
				if IsPure[1] != 1:
					self.attVal2.buildTree(currentDepth + 1)
				else:
				#if child node is pure, stop growing and make it leaf with pure class
					self.attVal2.value = MajorityClass[1]
		elif numOfClasses == 3:
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			if depth == 1: 
				self.attVal1.value = MajorityClass[0]
			else: 
				if IsPure[0] != 1:
					self.attVal1.buildTree(currentDepth + 1)
				else:
					self.attVal1.value = MajorityClass[0]
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			if depth == 1: 
				self.attVal2.value = MajorityClass[1]
			else: 
				if IsPure[1] != 1:
					self.attVal2.buildTree(currentDepth + 1)
				else:
					self.attVal2.value = MajorityClass[1]
			self.attVal3 = node()
			self.attVal3.parent = self
			self.attVal3.branchFromParent = 3
			if depth == 1: 
				self.attVal3.value = MajorityClass[2]
			else: 
				if IsPure[2] != 1:
					self.attVal3.buildTree(currentDepth + 1)
				else:
					self.attVal3.value = MajorityClass[2]
		else:
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			if depth == 1: 
				self.attVal1.value = MajorityClass[0]
			else: 
				if IsPure[0] != 1:
					self.attVal1.buildTree(currentDepth + 1)
				else:
					self.attVal1.value = MajorityClass[0]
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			if depth == 1: 
				self.attVal2.value = MajorityClass[1]
			else: 
				if IsPure[1] != 1:
					self.attVal2.buildTree(currentDepth + 1)
				else:
					self.attVal2.value = MajorityClass[1]
			self.attVal3 = node()
			self.attVal3.parent = self
			self.attVal3.branchFromParent = 3
			if depth == 1: 
				self.attVal3.value = MajorityClass[2]
			else: 
				if IsPure[2] != 1:
					self.attVal3.buildTree(currentDepth + 1)
				else:
					self.attVal3.value = MajorityClass[2]
			self.attVal4 = node()
			self.attVal4.parent = self
			self.attVal4.branchFromParent = 4
			if depth == 1: 
				self.attVal4.value = MajorityClass[3]
			else: 
				if IsPure[3] != 1:
					self.attVal4.buildTree(currentDepth + 1)
				else:
					self.attVal4.value = MajorityClass[3]
	#recursive method to find out next node in tree and build it from there in decision tree
	def buildTree(self, valDepth):
		#list to hold the columns we have already used in this path
		parents = []
		#list to hold the value of the columns used in this path
		branches = []
		#entropy of the node's parent
		entropyParent = self.parent.entropy
		label0 = label1 = 0
		loc = node()
		loc = self
		branches.append(loc.branchFromParent)
		#finds out all the ancestors of the node in order
		while loc.parent:
			loc = loc.parent
			parents.append(loc.value)
			#stores the branch values of the parents in order
			if loc.branchFromParent: 
				branches.append(loc.branchFromParent)
		selectedRows = []
		#finds the row numbers of the dataset which we will use now. Creates the reduced data set for us to use
		for i in range(0, rows):
			flag = 1
			for j in range(0, len(parents)):
				if myDataset[i][parents[j]] != branches[j]: 
					flag = 0
			if flag == 1: 
				selectedRows.append(i)
		reducedRows = len(selectedRows)
		#checks total number of examples for each class in the reduced dataset
		for i in range(0, reducedRows):
			if myDataset[selectedRows[i]][0] == 0:
				label0 += 1
			else:
				label1 += 1
		#the new node which will be formed will have this entropy
		entropyNode = entropyFunction(label0, label1)
		selectionCount = 0
		#figures out the column with maximum information gain
		for i in range(1, columns):
			if i not in parents:
				#finds out the number of different values this column takes
				diffClass = discreteValue[i]
				#creates a matrix which stores total number of examples for each different value of the column
				diffClassDiv = [[0 for x in range(2)] for y in range(diffClass)]
				for j in range(0, reducedRows):
					if myDataset[selectedRows[j]][0] == 0: 
						diffClassDiv[myDataset[selectedRows[j]][i] - 1][0] += 1
					else: 
						diffClassDiv[myDataset[selectedRows[j]][i] - 1][1] += 1
				entropyClass = 0
				majorityClass = []
				isPure = []
				#for every different value of the column
				for k in range(0, diffClass):
					#finds out majority class
					if diffClassDiv[k][0] < diffClassDiv[k][1]: 
						majorityClass.append(1) 
					else:
						majorityClass.append(0)
					#finds out if it is a pure node
					if diffClassDiv[k][0] == 0 or diffClassDiv[k][1] == 0:
						isPure.append(1)
					else:
						isPure.append(0)
					#calculates weighted entropy of column
					totalClass = diffClassDiv[k][0] + diffClassDiv[k][1]
					probClass = float(totalClass) / float(reducedRows)
					entropyClass = entropyClass + (float(probClass) * float(entropyFunction(diffClassDiv[k][0], diffClassDiv[k][1])))
				infoGain = entropyParent - entropyClass
				#inserting information gain into maxInfoGain only for the first attribute checked for 
				#comparing purposes with information gain of other columns
				if selectionCount == 0:
					maxInfoGain = infoGain
					selectedAttribute = i
					numOfClasses = diffClass
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
					selectionCount += 1
				#checking if new info gain is greater than previous max info gain
				if infoGain > maxInfoGain:
					maxInfoGain = infoGain
					selectedAttribute = i
					numOfClasses = diffClass
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
		#node value becomes column value with max info gain
		self.value = selectedAttribute
		self.entropy = entropyNode
		#checks number of branches that will appear from self node
		if numOfClasses == 2:
			#create child node from branch 1
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			#if depth is equal to input depth, stop growing and make it leaf with majority class
			if valDepth == depth: 
				self.attVal1.value = MajorityClass[0]
			else: 
				#if child node is not pure
				if IsPure[0] != 1:
					self.attVal1.buildTree(valDepth + 1)
				#if child node is pure, stop growing and make it leaf with pure class	
				else:
					self.attVal1.value = MajorityClass[0]
			#create child node from branch 2
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			#if depth is equal to input depth, stop growing and make it leaf with majority class
			if valDepth == depth: 
				self.attVal2.value = MajorityClass[1]
			else:
				#if child node is not pure
				if IsPure[1] != 1:
					self.attVal2.buildTree(valDepth + 1)
				#if child node is pure, stop growing and make it leaf with pure class
				else: 
					self.attVal2.value = MajorityClass[1]
		elif numOfClasses == 3:
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			if valDepth == depth: 
				self.attVal1.value = MajorityClass[0]
			else: 
				if IsPure[0] != 1:
					self.attVal1.buildTree(valDepth + 1)
				else:
					self.attVal1.value = MajorityClass[0]
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			if valDepth == depth: 
				self.attVal2.value = MajorityClass[1]
			else: 
				if IsPure[1] != 1:
					self.attVal2.buildTree(valDepth + 1)
				else:
					self.attVal2.value = MajorityClass[1]
			self.attVal3 = node()
			self.attVal3.parent = self
			self.attVal3.branchFromParent = 3
			if valDepth == depth: 
				self.attVal3.value = MajorityClass[2]
			else: 
				if IsPure[2] != 1:
					self.attVal3.buildTree(valDepth + 1)
				else:
					self.attVal3.value = MajorityClass[2]
		else:
			self.attVal1 = node()
			self.attVal1.parent = self
			self.attVal1.branchFromParent = 1
			if valDepth == depth: 
				self.attVal1.value = MajorityClass[0]
			else: 
				if IsPure[0] != 1:
					self.attVal1.buildTree(valDepth + 1)
				else:
					self.attVal1.value = MajorityClass[0]
			self.attVal2 = node()
			self.attVal2.parent = self
			self.attVal2.branchFromParent = 2
			if valDepth == depth: 
				self.attVal2.value = MajorityClass[1]
			else: 
				if IsPure[1] != 1:
					self.attVal2.buildTree(valDepth + 1)
				else:
					self.attVal2.value = MajorityClass[1]
			self.attVal3 = node()
			self.attVal3.parent = self
			self.attVal3.branchFromParent = 3
			if valDepth == depth: 
				self.attVal3.value = MajorityClass[2]
			else: 
				if IsPure[2] != 1:
					self.attVal3.buildTree(valDepth + 1)
				else:
					self.attVal3.value = MajorityClass[2]
			self.attVal4 = node()
			self.attVal4.parent = self
			self.attVal4.branchFromParent = 4
			if valDepth == depth: 
				self.attVal4.value = MajorityClass[3]
			else: 
				if IsPure[3] != 1:
					self.attVal4.buildTree(valDepth + 1)
				else:
					self.attVal4.value = MajorityClass[3]
	
	#method to print out each path of decision tree from root to leaf nodes along with the branch values
	def printAllPaths(self):
		nodeStack.append(self.value)
		branchStack.append(self.branchFromParent)
		if self.attVal1:
			self.attVal1.printAllPaths()
		if self.attVal2:
			self.attVal2.printAllPaths()
		if self.attVal3:
			self.attVal3.printAllPaths()
		if self.attVal4:
			self.attVal4.printAllPaths()
		if not self.attVal1 and not self.attVal2 and not self.attVal3 and not self.attVal4:
			for i in range(0, len(nodeStack)):
				if branchStack[i]:
					print "Branch",branchStack[i],"->",
				if i == len(nodeStack) - 1:
					print "Class",nodeStack[i]
				else:
					print "Node",nodeStack[i],"->",
		nodeStack.pop()
		branchStack.pop()
		
	#method to test the decision tree
	def testTree(self, count):
		#check value of root node
		currentColumn = self.value
		#check data in test data for row number = count and column number =  root value
		val = myTestDataset[count][currentColumn]
		#traverse the tree accordingly
		while True:
			if val == 1:
				self = self.attVal1
			elif val == 2:
				self = self.attVal2
			elif val == 3:
				self = self.attVal3
			else:
				self = self.attVal4
			#if node is leaf
			if not self.attVal1 and not self.attVal2 and not self.attVal3 and not self.attVal4:
				val = self.value
				break
			#else take the data in test data for row number = count and column number = value of the current node 
			val = myTestDataset[count][self.value]
		return val

#definition of class tree
class tree:
	def __init__(self):
		self.root = None

	def insertDecisionStump(self, data):
		self.root = node()
		self.root.insertDecisionStump(data)
		return True

	def printAllPaths(self):
		print "Printing All Paths from Root to Leaves"
		self.root.printAllPaths()
		return True

	def testTree(self, count):
		return self.root.testTree(count)

#method to find out entropy given the number of examples of each class
def entropyFunction(class0, class1):
	
	sumOfClasses = class0 + class1
	if sumOfClasses != 0:
		probClass0 = float(class0) / float(sumOfClasses)
		probClass1 = float(class1) / float(sumOfClasses)
	else: 
		probClass0 = probClass1 = 0
	if probClass0 != 0: 
		probClass0 = probClass0	* math.log(probClass0, 2)
	if probClass1 != 0: 
		probClass1 = probClass1 * math.log(probClass1, 2)
	result =  probClass0 + probClass1
	return (-1) * result

#create tree object
decisionTree = tree()
filename = "TrainingSet.txt"
print "Enter depth of tree:"
depth = int(raw_input())
#find number of examples in training data
rows = sum(1 for line in open(filename))
columns = 10
#build training dataset from file
myDataset = [[0 for x in range(columns)] for y in range(rows)]
myList = []
with open(filename, 'r') as fileObj:
	i = 0
	for line in fileObj:
		myList = line.split()
		for j in range(0, columns): 
			myDataset[i][j] = myList[j]
		i = i + 1
for i in range(0, rows):
	for j in range(0,columns): 
		myDataset[i][j] = float(myDataset[i][j])
for i in range(0, rows):
	for j in range(0,columns): 
		myDataset[i][j] = int(myDataset[i][j])
for i in range(0, rows):
	for j in range(1, columns):
		if myDataset[i][j] < 2.5:
			myDataset[i][j] = 1
		elif myDataset[i][j] > 2.5 and myDataset[i][j] < 5:
			myDataset[i][j] = 2
		elif myDataset[i][j] > 5 and myDataset[i][j] < 7.5:
			myDataset[i][j] = 3
		else:
			myDataset[i][j] = 4

#find number of examples for each class in training data
class0 = class1 = 0
for i in range(0, rows):
	if myDataset[i][0] == 1: 
		class1 += 1
	else: 
		class0 += 1

entropyTarget = entropyFunction(class0, class1)
discreteValue = []

#stores the number of different values each column takes
for i in range(0, columns):
	tempVar = []
	for j in range(0, rows):
		if myDataset[j][i] not in tempVar:
			tempVar.append(myDataset[j][i])
	discreteValue.append(len(tempVar))

maxInfoGain = 0
#checking for column value with maximum information gain
for attribute in range(1, columns):
	diffClass = discreteValue[attribute]
	diffClassDiv = [[0 for x in range(2)] for y in range(diffClass)]
	for row in range(0, rows):
		if myDataset[row][0] == 0: 
			diffClassDiv[myDataset[row][attribute] - 1][0] += 1
		else: 
			diffClassDiv[myDataset[row][attribute] - 1][1] += 1
	entropyClass = 0
	majorityClass = []
	isPure = []
	for i in range(0, diffClass):
		if diffClassDiv[i][0] < diffClassDiv[i][1]: 
			majorityClass.append(1) 
		else: 
			majorityClass.append(0)
		if diffClassDiv[i][0] == 0 or diffClassDiv[i][1] == 0:
			isPure.append(1)
		else:
			isPure.append(0)
		totalClass = diffClassDiv[i][0] + diffClassDiv[i][1]
		probClass = float(totalClass) / float(rows)
		entropyClass = entropyClass + (float(probClass) * float(entropyFunction(diffClassDiv[i][0], diffClassDiv[i][1])))
	infoGain = entropyTarget - entropyClass
	if infoGain > maxInfoGain:
		maxInfoGain = infoGain
		selectedAttribute = attribute
		numOfClasses = diffClass
		MajorityClass = []
		MajorityClass = majorityClass
		IsPure = []
		IsPure = isPure

#inserting root node into decision tree and building it from there
decisionTree.insertDecisionStump(selectedAttribute)
nodeStack = []
branchStack = []

#printing each and every path from root node to leaves
decisionTree.printAllPaths()

testName = "testSet.txt"
rows = sum(1 for line in open(testName))
columns = 10

#populating test dataset from file
myTestDataset = [[0 for x in range(columns)] for y in range(rows)]
i = 0
myList = []
with open(testName, 'r') as fileObj:
	for line in fileObj:
		myList = line.split()
		for j in range(0, 10): 
			myTestDataset[i][j] = myList[j]
		i = i + 1

#type casting from string to int
for i in range(0, rows):
	for j in range(0, columns):
		myTestDataset[i][j] = float(myTestDataset[i][j])
for i in range(0, rows):
	for j in range(0, columns):
		myTestDataset[i][j] = int(myTestDataset[i][j])

for i in range(0, rows):
	for j in range(1, columns):
		if myTestDataset[i][j] < 2.5:
			myTestDataset[i][j] = 1
		elif myTestDataset[i][j] > 2.5 and myTestDataset[i][j] < 5:
			myTestDataset[i][j] = 2
		elif myTestDataset[i][j] > 5 and myTestDataset[i][j] < 7.5:
			myTestDataset[i][j] = 3
		else:
			myTestDataset[i][j] = 4

count = correctPrediction = truePos = falsePos = trueNeg = falseNeg = 0

#for every example in test dataset, the tree is tested to find out prediction
for i in range(0, rows):
	prediction = decisionTree.testTree(count)
	#calculating number of true positives
	if myTestDataset[count][0] == 1 and prediction == 1:
		truePos += 1
		correctPrediction += 1
	#calculating number of false negatives
	elif myTestDataset[count][0] == 1 and prediction == 0:
		falseNeg += 1
	#calculating number of true negatives
	elif myTestDataset[count][0] == 0 and prediction == 0:
		trueNeg += 1
		correctPrediction += 1
	#calculating number of false positives
	else:
		falsePos += 1
	count += 1

accuracy = float(correctPrediction) / float(rows)
print "\n"
print "Accuracy : ", accuracy,"\n"
print "n  = ",rows,"\t","Predicted No","\t","Predicted Yes"
print "Actual No\t   ", trueNeg,"\t   ", falsePos
print "Actual Yes\t   ", falseNeg,"\t\t   ", truePos
print "Precision\t", float(truePos) / float(truePos + falsePos)
print "Recall\t\t", float(truePos) / float(truePos + falseNeg)