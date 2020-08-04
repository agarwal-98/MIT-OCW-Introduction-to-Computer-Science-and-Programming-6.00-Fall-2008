# Problem 1

# defining the function
def chickennuggetsolution(n):
# taking one value of a between 0 and the defined number, n. The 'n' helps as we don't need to subjectively decide what should be the last value of a that we need to test
  for a in range(0,n):
# for a value of a taken above, we now iterate over all the values of b
   for b in range(0,n):
# for a value of a and b, we now iterate over all values of c.
    for c in range(0,n):
# defining the tuple that will contain the relevant values of a, b and c for each n
      combinations = ()
      if 6*a + 9*b + 20*c == n:
        combinations = combinations + (a,b,c,n,)
        print (combinations)

# note we are resetting the tuple after every iteration to 
# give us a separate answer for a each combination


# defining the range of numbers to be tested for
for i in range(50,56):
  chickennuggetsolution(i)


# # given we can find combinations for 50-55, we are testing for 56-64
for vals in range(56,65):
  for i in range(50,56):
    if vals - i == 6:
      chickennuggetsolution(vals)
      break
    if vals - i == 9:
      chickennuggetsolution(vals)
      break
    if vals - i == 20:
      chickennuggetsolution(vals)
      break

# problem 2

# This theorem holds true because as long as the number of solutions found consecutively 
# equals the smallest multiplicative number (in this case, 6), subsequent solutions can 
# simply be found by adding this number to our previously found solutions.


# Problem 3

consecutive_count = 0
# counter to keep track of the consecutive number of solutions
# found so far
n=1
# defining the variable to be tested
count = 0
# the list which will save all the values for which on
# combination exists as requested by the question
while count <= 6:
  # the information i need to keep track of while I loop
  # through the possibilities
  solution = 0
 # defining this before looping starts - the condition I am
 # testing for
  for a in range(0,n):
    for b in range(0,n):
      for c in range(0,n):
        if 6*a + 9*b + 20*c == n:
          solution = 1
          break

# if a solution is found, increase the count 
  if solution == 1: 
    count += 1

# else, reset count to 0 and save the value of n as the largest so far
  else:
    count = 0
    largestval = n

 # increase count of n after every test
  n += 1

print ('largest number is', largestval)
# savedn[-1] extracts the last value from the list.


# # PROBLEM 4
      
bestSoFar = 0

# packages = (6,9,20)
# packages = (16,19, 20)
# packages = (4,9, 16)

for n in range(0,150):
  solution = 0
  # reducing the range of search
  for a in range(0,int(n/packages[0])+1):
   for b in range(0,int(n/packages[1])+1):
    for c in range(0,int(n/packages[2])+1):
      if packages[0]*a + packages[1]*b + packages[2]*c == n:
        solution = 1
        break
  if solution == 0 :
  # if a combination not found for an interation, the nth value is saved
    bestSoFar = n 

print ('largest number of mcnuggets that cannot be bought in exact quantity', bestSoFar)

