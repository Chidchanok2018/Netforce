import csv
import numpy as np
import pandas as pd

with open('test.csv') as csvfile:
	data = {}
	dataInArray = []
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	# print(spamreader)
	for row in spamreader:
		s = row[0].split(',')
		s[1] = int(s[1])
		print(s)
		data[s[0]] = s[1]
		dataInArray.append(s)
	# print(data)
	# print(dataInArray)
	# print()
	# print(dataInArray[0][0][:1])
	# print()
	
	# Highest Salary Function
	def highest_salary(data):
		salaryArray = []
		for value in data.values():
			salaryArray.append(value)
		max_value = max(salaryArray)
		max_value_index = salaryArray.index(max_value)
		for key, value in data.items():
			if value == max_value:
				print("{} is highest salary.".format(key))
	
	# Lowest Salary Function
	def lowest_salary(data):	
		salaryArray = []
		for value in data.values():
			salaryArray.append(value)
		min_value = min(salaryArray)
		min_value_index = salaryArray.index(min_value)
		for key, value in data.items():
			if value == min_value:
				print("{} is lowest salary.".format(key))
	
	# Average Salary Function
	def average_salary(data):
		salaryArray = []
		for value in data.values():
			salaryArray.append(value)
		average_value = sum(salaryArray) / len(salaryArray)
		print("Average Salary is {}".format(average_value))
	
	# Query with Salary Number
	def query_all(data):
		for key, value in sorted(data.iteritems(), key = lambda (k, v): (v, k), reverse=True):
			print("{} : {}".format(value, key))

	# Query by Name
	def query_name(data):
		for key in sorted(data.keys()):
			print("{} : {}".format(key, data[key]))

	# Query with First Word
	def query_first_char(dataInArray):
		# print(dataInArray)
		# firstChar = []
		# salary = []
		# firstCharIndex = []
		# newSolutionDict = {}
		newSolutionArray = []
		for dataSet in dataInArray:
			# print(dataSet[0][:1])
			newX = dataSet[0][:1]
			# print(dataSet[1])
			newY = dataSet[1]
			# newSolutionDict['name'] = dataSet[0][:1]
			# newSolutionDict['count'] = dataSet[1]
			update = {'name': newX, 'count': newY}
			# newSolutionDict.update(update)
			newSolutionArray.append(update)
		# print(newSolutionArray)
		df = pd.DataFrame(newSolutionArray)
		print(df['count'].groupby([df['name']]).sum())
		# from Stackoverflow
		
        def query_first_char_new(data):
            group = {}
            for key,val in data.items():
                key_g = key[0]
                group.setdefault(key_g,0)
                group[key_g] += val

            for key, value in group.items():
                print("{} : {}".format(key, value))

	# Main function
	print('')
	print('Highest Salary')
	highest_salary(data)
	print('')
	print('Lowest Salary')
	lowest_salary(data)
	print('')
	print('Average Salary')
	average_salary(data)
	print('')
	print('Order Data by Salary')
	query_all(data)
	print('')
	print('Order Data by name')
	query_name(data)
	print('')
	print('Group and Order Data By Name')
	query_first_char(dataInArray)
        print('')
        print('Group and Order Data By Name with setdefault method in Dict Data Structure')
        query_first_char_new(data)
