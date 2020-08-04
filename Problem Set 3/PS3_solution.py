# PS3


target = 'atgacatgcacaagtatgcat'
key = 'atgc'

from string import*

# probem 1

def countSubStringMatch(target,key): 
 # setting the index to start index at 0 to start looking for matches
 index = 0
 # initiating the variable, count, to keep track of the number of matches
 count = 0

 while index < len(target):
  possiblematch = target.find(key, index)
  if possiblematch != -1:
   count += 1   			
 # new index starts after the match was found
   index = len(key) + possiblematch
   print (index)

  else:
# if no match, no need to look anymore
   return count
 return count


def countSubStringMatchRecursive(target,key):
 count = 0
 possiblematch = target.find(key)
 if possiblematch == -1:
 # if no match, return 0
  return count
 else:
# if key is found match, the function goes back to the definition to find more matches

  count = 1 + countSubStringMatchRecursive(target[possiblematch+len(key):],key)
 return count


print (countSubStringMatch(target,key))
print (countSubStringMatchRecursive(target,key))

# # problem 2

def subStringMatchExact(target,key): 
 count = ()
	# initiating the tuple that will store the value
 index = 0
 if len(key) == 0:
 	return count
 else:
  while index < len(target):
   possiblematch = target.find(key, index)
   if possiblematch != -1:
    count = count + (possiblematch,)
    index = possiblematch + len(key)
			# does not return anything here as  I want the looping to continue till i dont find anything
   else:
    return count  
 return count

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def implementproblem2():
 print (subStringMatchExact(target1,key10))
 print (subStringMatchExact(target1,key11))
 print (subStringMatchExact(target1,key12))
 print (subStringMatchExact(target1,key13))
 print (subStringMatchExact(target2,key10))
 print (subStringMatchExact(target2,key11))
 print (subStringMatchExact(target2,key12))
 print (subStringMatchExact(target2,key13))



implementproblem2()


# problem 3



def subStringMatchOneSub(target,key):
	"""search for all locations of key in target, with one substitution"""
	allAnswers = ()
	for miss in range(0,len(key)):
		# miss picks location for missing element
		# key1 and key2 are substrings to match
		key1 = key[:miss]
		key2 = key[miss+1:]
		print ('breaking key',key,'into',key1,key2)
			# match1 and match2 are tuples of locations of start of matches
			# for each substring in target
		match1 = subStringMatchExact(target,key1)
		print ('this is match1 tuple', match1)
		match2 = subStringMatchExact(target,key2)
		print ('this is match2 tuple', match2)
			# when we get here, we have two tuples of start points
			# need to filter pairs to decide which are correct
		filtered = constrainedMatchPair(match1,match2,len(key1))
		allAnswers = allAnswers + filtered
		print ('match1',match1)
		print ('match2',match2)
		print ('possible matches for',key1,key2,'start at',filtered)
	return allAnswers
 


def constrainedMatchPair(start1,start2,m):
	constrainmatches = ()
	# if one tuple is empty, copy the other tuple
	if len(start1) == 0:
		constrainmatches = start2
	elif len(start2) == 0:
		constrainmatches = start1
	else:
		for n in start1:
			for k in start2:
				if n+m+1==k:
					constrainmatches = constrainmatches + (n,)
	return constrainmatches


subStringMatchOneSub(target,key)


# # probem 4


def subStringMatchExactlyOneSub(target,key):
	exactlyonesub = ()
	exactmatches = subStringMatchExact(target,key)
	print ( 'starting point for exact matches', exactmatches)
	uptoonesub = subStringMatchOneSub(target,key)
	print ('starting point for matches with upto one sub', uptoonesub)
	for index in uptoonesub:
		# if index not in the exact matches tuple, store the index 
		if index not in exactmatches:
			exactlyonesub = exactlyonesub + (index,)	
	print ('points with exactly one sub', exactlyonesub)
	return exactlyonesub


subStringMatchExactlyOneSub(target,key)
