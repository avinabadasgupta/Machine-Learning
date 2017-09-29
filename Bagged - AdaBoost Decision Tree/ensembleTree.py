#Applied Machine Learning - B659
#Programming Assignment 2
#Developed and submitted by Avinaba Dasgupta
#Code for implementing Bagging and Boosting in Decision Tree
#Version 1.1
import math
import csv
import random
import sys
import os
from numpy.random import RandomState

#definition of node class
class node:
	def __init__(self):
		#column number of node
		self.value   			= None
		#parent column number of node
		self.parent  			= None
		#each node has maximum 2 children nodes
		self.left 				= None
		self.right 				= None
		#entropy of node
		self.entropy    		= None
		#value of connecting branch of parent and child
		self.branchFromParent 	= None
	
	#method to create the decision stump or root node of Boosted decision tree	
	def insertBoostedDecisionStump(self, data):
		self.value = data
		self.entropy = entropyTarget
		currentDepth = 1
		#create child node from branch 1
		self.left = node()
		self.left.parent = self
		self.left.branchFromParent = 0
		#if input depth is 1, stop growing and make it leaf with majority class
		if depth == 1: 
			self.left.value = MajorityClass[0]
		else: 
			#if child node is not pure
			if IsPure[0] != 1:
				self.left.buildBoostedTree(currentDepth + 1)
			else:
			#if child node is pure, stop growing and make it leaf with pure class	
				self.left.value = MajorityClass[0]
		#create child node from branch 2
		self.right = node()
		self.right.parent = self
		self.right.branchFromParent = 1
		#if input depth is 1, stop growing and make it leaf with majority class
		if depth == 1: 
			self.right.value = MajorityClass[1]
		else:
			#if child node is not pure
			if IsPure[1] != 1:
				self.right.buildBoostedTree(currentDepth + 1)
			else:
			#if child node is pure, stop growing and make it leaf with pure class
				self.right.value = MajorityClass[1]

	#method to create the decision stump or root node of Bagged decision tree	
	def insertBaggedDecisionStump(self, data):
		self.value = data
		self.entropy = entropyTarget
		currentDepth = 1
		#create child node from branch 1
		self.left = node()
		self.left.parent = self
		self.left.branchFromParent = 1
		#if input depth is 1, stop growing and make it leaf with majority class
		if depth == 1: 
			self.left.value = MajorityClass[0]
		else: 
			#if child node is not pure
			if IsPure[0] != 1:
				self.left.buildBaggedTree(currentDepth + 1)
			else:
			#if child node is pure, stop growing and make it leaf with pure class	
				self.left.value = MajorityClass[0]
		#create child node from branch 2
		self.right = node()
		self.right.parent = self
		self.right.branchFromParent = 2
		#if input depth is 1, stop growing and make it leaf with majority class
		if depth == 1: 
			self.right.value = MajorityClass[1]
		else:
			#if child node is not pure
			if IsPure[1] != 1:
				self.right.buildBaggedTree(currentDepth + 1)
			else:
			#if child node is pure, stop growing and make it leaf with pure class
				self.right.value = MajorityClass[1]
		
	#recursive method to find out next node in tree and build it from there in Boosted decision tree
	def buildBoostedTree(self, valDepth):
		#list to hold the columns we have already used in this path
		parents = []
		#list to hold the value of the columns used in this path
		branches = []
		#entropy of the node's parent
		entropyParent = self.parent.entropy
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
				if newDataset[i][parents[j]] != branches[j]: 
					flag = 0
			if flag == 1: 
				selectedRows.append(i)
		reducedRows = len(selectedRows)
		#checks total number of examples for each class in the reduced dataset
		#checks total weight of examples for each class in the reduced dataset
		weight_0 = weight_1 = 0
		sum_class_0 = sum_class_1 = 0
		
		for i in range(0, reducedRows):
			if newDataset[selectedRows[i]][0] == 0:
				weight_0 += weight[i]
				sum_class_0 += 1
			
			else:
				weight_1 += weight[i]
				sum_class_1 += 1
		
		#the new node which will be formed will have this entropy
		entropyNode = boostedEntropyFunction(sum_class_0, sum_class_1, weight_0, weight_1)
		selectionCount = 0
		
		#figures out the column with maximum information gain
		for i in range(1, columns):
			if i not in parents:
				totalWeight = weightVal0Class0 = weightVal0Class1 = weightVal1Class1 = weightVal1Class0 = 0
				#creates a matrix which stores total number of examples for each different value of the column
				diffClassDiv = [[0 for x in range(2)] for y in range(2)]
				for j in range(0, reducedRows):
					if newDataset[selectedRows[j]][0] == 0: 
						diffClassDiv[newDataset[selectedRows[j]][i]][0] += 1
						if newDataset[selectedRows[j]][i] == 0:
							totalWeight += weight[row]
							weightVal0Class0 += weight[row]
						else:
							totalWeight += weight[row]
							weightVal1Class0 += weight[row]
					else: 
						diffClassDiv[newDataset[selectedRows[j]][i]][1] += 1
						if newDataset[selectedRows[j]][i] == 0:
							totalWeight += weight[row]
							weightVal0Class1 += weight[row]
						else:
							totalWeight += weight[row]
							weightVal1Class1 += weight[row]
				
				entropyClass = 0
				majorityClass = []
				isPure = []
				#for every different value of the column
				for k in range(0, 2):
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
					
					if k == 0:
						prior = float(weightVal0Class0 + weightVal0Class1) / float(totalWeight)
						entropyClass = entropyClass+(prior * float(boostedEntropyFunction(diffClassDiv[0][0], diffClassDiv[0][1], 
																weightVal0Class0, weightVal0Class1)))
					else:
						prior = float(weightVal0Class0 + weightVal0Class1) / float(totalWeight)
						entropyClass = entropyClass+(prior * float(boostedEntropyFunction(diffClassDiv[0][0], diffClassDiv[0][1], 
																weightVal0Class0, weightVal0Class1)))
				
				infoGain = entropyParent - entropyClass
				#inserting information gain into maxInfoGain only for the first attribute checked for 
				#comparing purposes with information gain of other columns
				if selectionCount == 0:
					maxInfoGain = infoGain
					selectedAttribute = i
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
					selectionCount += 1
				#checking if new info gain is greater than previous max info gain
				if infoGain > maxInfoGain:
					maxInfoGain = infoGain
					selectedAttribute = i
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
		#node value becomes column value with max info gain
		self.value = selectedAttribute
		self.entropy = entropyNode
		#create child node from branch 1
		self.left = node()
		self.left.parent = self
		self.left.branchFromParent = 1
		#if depth is equal to input depth, stop growing and make it leaf with majority class
		if valDepth == depth: 
			self.left.value = MajorityClass[0]
		else: 
			#if child node is not pure
			if IsPure[0] != 1:
				self.left.buildBoostedTree(valDepth + 1)
			#if child node is pure, stop growing and make it leaf with pure class	
			else:
				self.left.value = MajorityClass[0]
		#create child node from branch 2
		self.right = node()
		self.right.parent = self
		self.right.branchFromParent = 2
		#if depth is equal to input depth, stop growing and make it leaf with majority class
		if valDepth == depth: 
			self.right.value = MajorityClass[1]
		else:
			#if child node is not pure
			if IsPure[1] != 1:
				self.right.buildBoostedTree(valDepth + 1)
			#if child node is pure, stop growing and make it leaf with pure class
			else: 
				self.right.value = MajorityClass[1]

	#recursive method to find out next node in tree and build it from there in Bagged decision tree
	def buildBaggedTree(self, valDepth):
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
				#creates a matrix which stores total number of examples for each different value of the column
				diffClassDiv = [[0 for x in range(2)] for y in range(2)]
				for j in range(0, reducedRows):
					if myDataset[selectedRows[j]][0] == 0: 
						diffClassDiv[myDataset[selectedRows[j]][i] - 1][0] += 1
					else: 
						diffClassDiv[myDataset[selectedRows[j]][i] - 1][1] += 1
				entropyClass = 0
				majorityClass = []
				isPure = []
				#for every different value of the column
				for k in range(0, 2):
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
					numOfClasses = 2
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
					selectionCount += 1
				#checking if new info gain is greater than previous max info gain
				if infoGain > maxInfoGain:
					maxInfoGain = infoGain
					selectedAttribute = i
					numOfClasses = 2
					MajorityClass = []
					MajorityClass = majorityClass
					IsPure = []
					IsPure = isPure
		#node value becomes column value with max info gain
		self.value = selectedAttribute
		self.entropy = entropyNode
		#create child node from branch 1
		self.left = node()
		self.left.parent = self
		self.left.branchFromParent = 1
		#if depth is equal to input depth, stop growing and make it leaf with majority class
		if valDepth == depth: 
			self.left.value = MajorityClass[0]
		else: 
			#if child node is not pure
			if IsPure[0] != 1:
				self.left.buildBaggedTree(valDepth + 1)
			#if child node is pure, stop growing and make it leaf with pure class	
			else:
				self.left.value = MajorityClass[0]
		#create child node from branch 2
		self.right = node()
		self.right.parent = self
		self.right.branchFromParent = 2
		#if depth is equal to input depth, stop growing and make it leaf with majority class
		if valDepth == depth: 
			self.right.value = MajorityClass[1]
		else:
			#if child node is not pure
			if IsPure[1] != 1:
				self.right.buildBaggedTree(valDepth + 1)
			#if child node is pure, stop growing and make it leaf with pure class
			else: 
				self.right.value = MajorityClass[1]
	
	#method to test the Boosted decision tree
	def testBoostedTree(self, count):
		#check value of root node
		currentColumn = self.value
		#check data in test data for row number = count and column number =  root value
		val = myTestDataset[count][currentColumn]
		#traverse the tree accordingly
		while True:
			if val == 0:
				self = self.left
			else:
				self = self.right
			#if node is leaf
			if not self.left and not self.right:
				val = self.value
				break
			#else take the data in test data for row number = count and column number = value of the current node 
			val = myTestDataset[count][self.value]
		return val

	#method to test the Bagged decision tree
	def testBaggedTree(self, count):
		#check value of root node
		currentColumn = self.value
		#check data in test data for row number = count and column number =  root value
		val = myTestDataset[count][currentColumn]
		#traverse the tree accordingly
		while True:
			if val == 1:
				self = self.left
			else:
				self = self.right
			
			#if node is leaf
			if not self.left and not self.right:
				val = self.value
				break
			#else take the data in test data for row number = count and column number = value of the current node 
			val = myTestDataset[count][self.value]
		return val

	#method to calculate the errors in training set in Boosted Tree
	def traverseBoostedTree(self, count):
		#check value of root node
		currentColumn = self.value
		#check data in test data for row number = count and column number =  root value
		val = newDataset[count][currentColumn]
		#traverse the tree accordingly
		while True:
			if val == 0:
				self = self.left
			else:
				self = self.right
			#if node is leaf
			if not self.left and not self.right:
				val = self.value
				break
			#else take the data in test data for row number = count and column number = value of the current node 
			val = newDataset[count][self.value]
		return val

#definition of class tree
class tree:
	def __init__(self):
		self.root = None

	def insertBoostedDecisionStump(self, data):
		self.root = node()
		self.root.insertBoostedDecisionStump(data)
		return True

	def insertBaggedDecisionStump(self, data):
		self.root = node()
		self.root.insertBaggedDecisionStump(data)
		return True
	
	def testBoostedTree(self, count):
		return self.root.testBoostedTree(count)

	def testBaggedTree(self, count):
		return self.root.testBaggedTree(count)

	def traverseBoostedTree(self, count):
		return self.root.traverseBoostedTree(count)

#method to calculate entropy
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

#method to calculate weighted entropy
def boostedEntropyFunction(classCount0, classCount1, weight0, weight1):
	sumOfClasses = classCount0 + classCount1
	if sumOfClasses != 0:
		probClass0 = float(weight0) / float(weight0 + weight1)
		probClass1 = float(weight1) / float(weight0 + weight1)
	else:
		probClass0 = probClass1 = 0
	if probClass0 != 0:
		probClass0 = probClass0	* math.log(probClass0, 2)
	if probClass1 != 0:
		probClass1 = probClass1 * math.log(probClass1, 2)
	result =  probClass0 + probClass1
	return (-1) * result

#method to load data from file into matrix data structure
def load_and_split_data(datapath):
	if datapath == 'agaricuslepiotatrain1.csv':
		rows = sum(1 for line in open(filename1))
		columns = 127
		#build training dataset from file
		myDataset = [[0 for x in range(columns)] for y in range(rows)]
		myList = []
		with open(filename1, 'r') as fileObj:
			reader = csv.reader(fileObj)
			i = 0
			for line in reader:
				myList = line
				for j in range(0, columns):
					myDataset[i][j] = myList[j]
				i += 1
		a = b = 0
		for i in range(0, rows):
			if i != 0:
				b = 0
				for j in range(0, columns):
					if j != 21:
						newDataset[a][b] = myDataset[i][j]
						b += 1
				a += 1
		rows -= 1
		columns -= 1
		for i in range(0, rows):
			for j in range(0,columns): 
				newDataset[i][j] = int(newDataset[i][j])
		for i in range(0, rows):
			temp = newDataset[i][0]
			newDataset[i][0] = newDataset[i][20]
			newDataset[i][20] = temp
		if entype == 'bag':
			for j in range(1, columns):
				for i in range(0, rows):
					newDataset[i][j] += 1
		rows += 1
		columns += 1
	else:
		testRows = sum(1 for line in open(filename2))
		testColumns = 127
		#build test dataset from file
		myDataset = [[0 for x in range(testColumns)] for y in range(testRows)]
		myList = []
		with open(filename2, 'r') as fileObj:
			reader = csv.reader(fileObj)
			i = 0
			for line in reader:
				myList = line
				for j in range(0, testColumns):
					myDataset[i][j] = myList[j]
				i += 1
		a = b = 0
		for i in range(0, testRows):
			if i != 0:
				b = 0
				for j in range(0, testColumns):
					if j != 21:
						myTestDataset[a][b] = myDataset[i][j]
						b += 1
				a += 1
		testRows -= 1
		testColumns -= 1
		for i in range(0, testRows):
			for j in range(0,testColumns): 
				myTestDataset[i][j] = int(myTestDataset[i][j])
		for i in range(0, testRows):
			temp = myTestDataset[i][0]
			myTestDataset[i][0] = myTestDataset[i][20]
			myTestDataset[i][20] = temp
		if entype == 'bag':
			for j in range(1, testColumns):
				for i in range(0, testRows):
					myTestDataset[i][j] += 1
		testRows += 1
		testColumns += 1

entype = sys.argv[1]
depth = int(sys.argv[2]);
bags = int(sys.argv[3]);
filename1 = sys.argv[4];
filename2 = 'agaricuslepiotatest1.csv'

rows = sum(1 for line in open(filename1))
columns = 127
testRows = sum(1 for line in open(filename2))
testColumns = 127
newDataset = [[0 for x in range(columns - 1)] for y in range(rows - 1)]
myTestDataset = [[0 for x in range(testColumns - 1)] for y in range(testRows - 1)]
load_and_split_data(filename1)
state = RandomState()
rows -= 1
testRows -= 1
columns = 126
testColumns = 126
decisionTree = [0 for x in range(bags)]

if entype == "bag":
	rowList = [[0 for x in range(rows)] for y in range(10)]
	r = random.Random()
	r.seed()
	for i in range(0, 10):
		for j in range(0, rows):
			rowList[i][j] = state.randint(0, rows - 1)
	for bag in range(0, bags):
		#print rows, columns
		myDataset = [[0 for x in range(columns)] for y in range(rows)]
		#print len(rowList)
		for i in range(0, rows):
			for j in range(0, columns):
				#print "rownum", rowList[i], "col num", j
				myDataset[i][j] = newDataset[rowList[bag][i]][j]
		#find number of examples for each class in training data
		class0 = class1 = 0
		for i in range(0, rows):
			if myDataset[i][0] == 1: 
				class1 += 1
			else: 
				class0 += 1
		entropyTarget = entropyFunction(class0, class1)
		maxInfoGain = 0
		#checking for column value with maximum information gain
		for attribute in range(1, columns):
			diffClassDiv = [[0 for x in range(2)] for y in range(2)]
			for row in range(0, rows):
				if myDataset[row][0] == 0: 
					diffClassDiv[myDataset[row][attribute] - 1][0] += 1
				else: 
					diffClassDiv[myDataset[row][attribute] - 1][1] += 1
			entropyClass = 0
			majorityClass = []
			isPure = []
			for i in range(0, 2):
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
				numOfClasses = 2
				MajorityClass = []
				MajorityClass = majorityClass
				IsPure = []
				IsPure = isPure
		#create tree object
		decisionTree[bag] = tree()
		#inserting root node into decision tree and building it from there
		decisionTree[bag].insertBaggedDecisionStump(selectedAttribute)
	load_and_split_data(filename2)
	correctPrediction = truePos = falsePos = trueNeg = falseNeg = 0
	#for every example in test dataset, the tree is tested to find out prediction
	for i in range(0, testRows):
		vote = []
		for bag in range(0, bags):
			prediction = decisionTree[bag].testBaggedTree(i)
			vote.append(prediction)
		class_0 = class_1 = 0
		for j in range(0, bags):
			if vote[j] == 0:
				class_0 += 1
			else:
				class_1 += 1
		if class_0 > class_1:
			prediction = 0
		else:
			prediction = 1
		#calculating number of true positives
		if myTestDataset[i][0] == 1 and prediction == 1:
				truePos += 1
				correctPrediction += 1
		#calculating number of false negatives
		elif myTestDataset[i][0] == 1 and prediction == 0:
			falseNeg += 1
		#calculating number of true negatives
		elif myTestDataset[i][0] == 0 and prediction == 0:
			trueNeg += 1
			correctPrediction += 1
		#calculating number of false positives
		else:
			falsePos += 1
	accuracy = float(correctPrediction) / float(testRows)
	print "Accuracy : ", accuracy,"\n"
	
else:
	#create initial weight vector
	Weight = float(1.0) / float(rows)
	weight = [Weight for x in range(rows)]
	alpha = []
	for bag in range(0, bags):
		weight_0 = weight_1 = 0
		sum_class_0 = sum_class_1 = 0
		#find number of examples and total weight for each class in training data
		for i in range(0, rows):
			if newDataset[i][0] == 1:
				weight_1 += weight[i]
				sum_class_1 += 1
			else: 
				weight_0 += weight[i]
				sum_class_0 += 1
	
		entropyTarget = boostedEntropyFunction(sum_class_0, sum_class_1, weight_0, weight_1)
		maxInfoGain = 0
	
		#checking for column value with maximum information gain
		for attribute in range(1, columns):
		
			totalWeight = weightVal0Class0 = weightVal0Class1 = weightVal1Class1 = weightVal1Class0 = 0
			diffClassDiv = [[0 for x in range(2)] for y in range(2)]
		
			for row in range(0, rows):
				if newDataset[row][0] == 0: 
					diffClassDiv[newDataset[row][attribute]][0] += 1
					if newDataset[row][attribute] == 0:
						totalWeight += weight[row]
						weightVal0Class0 += weight[row]
					else:
						totalWeight += weight[row]
						weightVal1Class0 +=  weight[row]
				else: 
					diffClassDiv[newDataset[row][attribute]][1] += 1
					if newDataset[row][attribute] == 0:
						totalWeight += weight[row]
						weightVal0Class1 += weight[row]
					else:
						totalWeight += weight[row]
						weightVal1Class1 += weight[row]
		
			entropyClass = 0
			majorityClass = []
			isPure = []
		
			for i in range(0, 2):
				if diffClassDiv[i][0] < diffClassDiv[i][1]: 
					majorityClass.append(1) 
				else: 
					majorityClass.append(0)
				if diffClassDiv[i][0] == 0 or diffClassDiv[i][1] == 0:
					isPure.append(1)
				else:
					isPure.append(0)
			
				if i == 0:
					prior = float(weightVal0Class0 + weightVal0Class1) / float(totalWeight)
					entropyClass = entropyClass+(prior * float(boostedEntropyFunction(diffClassDiv[0][0], diffClassDiv[0][1], 
																weightVal0Class0, weightVal0Class1)))
				else:
					prior = float(weightVal1Class0 + weightVal1Class1) / float(totalWeight)
					entropyClass = entropyClass+(prior * float(boostedEntropyFunction(diffClassDiv[1][0], diffClassDiv[1][1], 
																weightVal1Class0, weightVal1Class1)))
			infoGain = entropyTarget - entropyClass
			#print "infogain", infoGain
			if infoGain > maxInfoGain:
				maxInfoGain = infoGain
				selectedAttribute = attribute
				MajorityClass = []
				MajorityClass = majorityClass
				IsPure = []
				IsPure = isPure
		
		#create tree object
		decisionTree[bag] = tree()
		#inserting root node into decision tree and building it from there
		decisionTree[bag].insertBoostedDecisionStump(selectedAttribute)
		incorrectPrediction = 0
		incorrectList = []
		#for every example in test dataset, the tree is tested to find out prediction
		for i in range(0, rows):
			prediction = decisionTree[bag].traverseBoostedTree(i)
			#calculating number of true positives
			if newDataset[i][0] == 1 and prediction == 0:
				incorrectPrediction += 1
				incorrectList.append(i)
			#calculating number of false negatives
			elif newDataset[i][0] == 0 and prediction == 1:
				incorrectPrediction += 1
				incorrectList.append(i)
			else:
				pass

		#calculate error and alpha and z constant
		error = float(incorrectPrediction) / float(rows)
		x = (1 - float(error)) / error
		x = (math.log(x, 2)) / 2
		alpha.append(x)
		z = 2 * math.sqrt(float(error) * (1 - float(error)))
	
		for i in range(0, rows):
			if i in incorrectList:
				weight[i] = weight[i] * (math.exp(alpha[bag]) / z)
			else:
				weight[i] = weight[i] * (math.exp( - alpha[bag]) / z)

		#stopping criteria for boosting
		if bag > 0:
			if alpha[bag] == alpha[bag - 1]:
				bagCount = bag
				break

	load_and_split_data(filename2)
	count = correctPrediction = truePos = falsePos = trueNeg = falseNeg = 0
	prediction = 0
	#for every example in test dataset, the tree is tested to find out prediction
	for i in range(0, testRows):
		for bag in range(0, bagCount):
			pred = decisionTree[bag].testBoostedTree(i)
			if pred == 1:
				prediction = prediction + (alpha[bag] * 1)
			else:
				prediction = prediction + (alpha[bag] * (- 1))
		if prediction >= 0:
			prediction = 1
		else:
			prediction = 0
		#calculating number of true positives
		if myTestDataset[i][0] == 1 and prediction == 1:
			truePos += 1
			correctPrediction += 1
		#calculating number of false negatives
		elif myTestDataset[i][0] == 1 and prediction == 0:
			falseNeg += 1
		#calculating number of true negatives
		elif myTestDataset[i][0] == 0 and prediction == 0:
			trueNeg += 1
			correctPrediction += 1
		#calculating number of false positives
		else:
			falsePos += 1

	accuracy = float(correctPrediction) / float(testRows)
	print "Accuracy : ", accuracy