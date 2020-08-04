# QUESTION 1

def nestEggFixed(salary,save,growthrate,years):
	# retirement fund after end of year 1
	retirementfund = [salary*save*0.01]
	count = 1
	while count < years:
		# retirement fund after end of each year
		endofyear = retirementfund[count-1]*(1 +0.01*growthrate) + salary*save*0.01
		retirementfund.append(endofyear)
		count = count + 1
	return retirementfund




# QUESTION 2

def nestEggVariable(salary,save, growthrate):
	retirementfund = [salary*save*0.01]
	count = 1
	# making sure count does not exceed number of growthrates 
	while count < len(growthrate):
		endofyear = retirementfund[count-1]*(1 +0.01*growthrate[count]) + salary*save*0.01
		retirementfund.append(endofyear)
		count = count + 1
	return retirementfund




# QUESTION 3

def postretirement(savings,growthRates,expenses):
	# retirement fund net of expenses at the end of year 1
	firstyear = savings*(1 + 0.01*growthRates[0]) - expenses
	retirementfund = [firstyear]
	count = 1
	while count < len(growthRates):
		# calculating retirement fund after end of each year net of expenses
		endofyear = retirementfund[count-1]*(1 + 0.01*growthRates[count]) - expenses
		retirementfund.append(endofyear)
		count = count + 1
	return retirementfund




# QUESTION 4

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,postRetireGrowthRates, epsilon)
    print (expenses)

def findMaxExpenses(salary,save,preRetireGrowthRates,postRetireGrowthRates,epsilon):
	# cumulative savings till retirement
	savings = nestEggVariable(salary,save,preRetireGrowthRates)
	low = 0
	high = savings[-1]
	# initial expense is set at half of the savings
	expense = (low+high)/2.0
	ctr = 1
	# postretirement(savings,postRetireGrowthRates,expense)
	leftfunds = postretirement(savings[-1],postRetireGrowthRates,expense)
	# if retirement fund has an amount greater than epsilon, execute the following
	while abs(leftfunds[-1]) > epsilon:
		# if the amount of funds left is negative, set a lower expense amount
		if leftfunds[-1] < 0:
			high = expense
		else:
			low = expense
		expense = (low+high)/2.0
		# compute the new post retirement fund 
		leftfunds = postretirement(savings[-1],postRetireGrowthRates,expense)
		# keeping track of the number of iterations over the while loop
		ctr += 1
	print (ctr)
	return expense


def postretirement(savings,postRetireGrowthRates,expense):
	# post retirement fund at the end of first year net of expenses
	firstyear = (savings)*(1 + 0.01*postRetireGrowthRates[0]) - expense
	postretirementfund = [firstyear]
	count = 1
	while count < len(postRetireGrowthRates):
		# post retirement fund after end of each year net of expenses
		endofyear = postretirementfund[count-1]*(1 + 0.01*postRetireGrowthRates[count]) - expense
		postretirementfund.append(endofyear)
		count = count + 1
	return postretirementfund



# problem 1
print (nestEggFixed(10000,10,15,5))

# problem 2
salary      = 10000
save        = 10
growthRates = [3, 4, 5, 0, 3]
print (nestEggVariable(salary,save,growthRates))

# problem 3
savings     = 100000
growthRates = [10, 5, 0, 5, 1]
expenses    = 30000
print (postretirement(savings,growthRates,expenses))

# problem 4
testFindMaxExpenses()
