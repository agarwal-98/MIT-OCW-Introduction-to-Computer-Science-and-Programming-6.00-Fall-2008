# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1


#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subject_dict = {}
    # t = filename.split(',').strip()
    for line in inputFile:
        # line.strip()
        line = line.strip().split(',')
        # for i in line[1:]:
        #     i = int(i)
        subject_dict[(line[0])] = (int(line[1]),int(line[2]))
        # for k,v in document.items():
        #     for value in v:
        #         value = int(value)

    return subject_dict

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

# print loadSubjects(SUBJECT_FILENAME)
mydict = loadSubjects(SUBJECT_FILENAME)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    # subNames.sort()
    # print (subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        # val = int(val)
        # print 'this is val', val
        # print type(val)
        work = subjects[s][WORK]
        # work = int(work)
        # print type(work)
        # print 'this is work', work
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


#  ------------------------------------------------------------------------------

# Problem 2: Subject Selection By Greedy Optimization


def sort_subjects(filename, comparator):
    # list of all subjects
    subjects = list(filename.keys())
    # print (subjects)
    for i in range(len(subjects)):
        # current index equals i and is also the index with the max value
        max_index = i
        max_value =  subjects[i]
        # next index = current index + 1
        next_index = i + 1
        while next_index < len(subjects):
            if comparator(filename[subjects[next_index]],filename[subjects[max_index]]):
                # if comparator returns true, change the index and value
                max_index = next_index
                max_value = subjects[next_index]
            # increase index by 1
            next_index += 1

        # temporarily store the value of ith index of the subjects list
        temp = subjects[i]
        # replace the value of the ith index of the subject list with the highest value of the max index
        subjects[i] = subjects[max_index]
        # swap the value of the max index with the value of the ith index temporarily stored earlier
        subjects[max_index] = temp

    return subjects

#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    sorted_subjects = sort_subjects(subjects, comparator)

    work_done = 0
    greedy_dict = {}
    # while work_done < maxWork:
    #     for i in sorted_subjects:
    for i in sorted_subjects:
            # if value of work for a subject is less than total value of work left, store values in a dict 
            if subjects[i][WORK] <= (maxWork - work_done):
                greedy_dict[i] = subjects[i]
                work_done = work_done + subjects[i][WORK]

    return greedy_dict
#  --------------------------------------------------------------------------

print ('greedy advisor output', greedyAdvisor(mydict, 4, cmpWork))


# Problem 3: Subject Selection By Brute Force

def bruteForceAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[list(nameList)[i]] = list(tupleList)[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            return subset[:], subsetValue       
        else:

            return bestSubset, bestSubsetValue       
    else:
        s = list(subjects)[i]
        # print subjects
        # print 'my s', s
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            # print 'my subset', subset
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

# print ('brute force advisor output', bruteForceAdvisor(mydict, 4,cmpWork))


def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    # creating an empty list that will hold time values for a range of MaxWork values
    recorded_time = []
    # setting initial work time
    hour = 1
    # setting max work time
    maxWork = 2
    while hour <= maxWork:
        start_time = time.time()
        bruteForceAdvisor(mydict, hour, cmpWork)
        end_time = time.time()
        total_time = float('%0.2f' % (end_time - start_time))
        # appending total time taken to the list 
        recorded_time.append(total_time)
        hour += 1

    return recorded_time

print ('brute force time taken', bruteForceTime())

# brute force time for 4 hours of work = 2.38 seconds
# brute force time for 5 hours of work = 7.96 seconds
# brute force time for 6 hours of work = 28.92 seconds

# The brute force time takes a considerable amount of time to run for even small values of maxwork
# The largest maxwork will depend on several criterias such as inportance of quality results, downfalls
# of inaccurate output etc. Given that students pay quite a hefty sum for education, univerisities can afford
# to run a brute force algorithm for a few minutes to compapre/contrast varying results and optimize courses for
# their students accordingly.

#  -------------------------------------------------------------------------


# Problem 4: Subject Selection By Dynamic Programming
# numCalls = 0

def dpAdvisor(subjects, maxWork):
#     Returns a dictionary mapping subject name to (value, work) that contains a
#  set of subjects that provides the maximum value without exceeding maxWork.
#  subjects: dictionary mapping subject name to (value, work)
#  maxWork: int >= 0
#  returns: dictionary mapping subject name to (value, work)
#  """
# # TODO...
    m = {}
    final_dict = {}
    global WORK
    global VALUE
    mykeys = subjects.keys()
    myvalues = subjects.values()
    work = []
    value = []

    for each in mykeys:
        work.append(subjects[each][WORK])
        value.append(subjects[each][VALUE])

    result = fastadvisor(work, value, len(subjects)-1, maxWork, m)
    vals,keys = fastadvisor(work, value, len(subjects)-1, maxWork, m)  
    
    for each in keys:
        final_dict[list(mykeys)[each]] = (value[each],work[each])

    return final_dict



def fastadvisor(work, value, i, aWork, m):
# dynamic programming helper code for the above function
    try: return m[(i, aWork)]
    except KeyError:
        # base case 
        if i == 0:
            if work[i] <= aWork:
            # using memoization to store the value for future use
                m[(i, aWork)] = value[i], [i]
                return value[i], [i]
            else:
                m[(i, aWork)] = 0, []
                return 0, []
        # computing value if we were to not take the value of the ith element
        without_i, result_keys = fastadvisor(work, value, i-1, aWork, m)
        if work[i] > aWork:
            m[(i, aWork)] = without_i, result_keys
            return without_i, result_keys
        else: 
            with_i, result_keys_temp = fastadvisor(work, value, i-1, aWork - work[i], m)
            with_i += value[i]

        # checking if the max value is obtained with the ith element or without the ith element
        if with_i > without_i:
            i_value = with_i
            result_keys = [i] + result_keys_temp

        else:
            i_value = without_i

        m[(i, aWork)] = i_value, result_keys

        # returns the max value
        return i_value, result_keys


def dpTime():

# Runs tests on dpAdvisor and measures the time required to compute an
# sanswer.
    record_time = []
    hour = 1
    maxWork = 100
    while hour <= maxWork:
        start_time = time.time()
        dpAdvisor(mydict, hour)
        end_time = time.time()
        total_time = float('%0.2f' % (end_time - start_time))
        record_time.append(total_time)
        hour += 1

    return record_time


# -----------------------------------------------------------------

print ('dynamic programming output', dpAdvisor(mydict, 4))
print ('time taken with DP', dpTime())


# dynamic programming time for 4 hours of work = 0.00 seconds
# dynamic programming time for 8 hours of work = 0.00 seconds
# dynamic programming time for 12 hours of work = 0.02 seconds
# dynamic programming time for 20 hours of work = 0.02 seconds
# dynamic programming time for 35 hours of work = 0.02 seconds
# dynamic programming time for 50 hours of work = 0.05 seconds
# dynamic programming time for 100 hours of work = 0.13 seconds


# dynamic programming significantly faster than brute force. Evem for upto 100 hours
# of work it takes less than a second to produce the output!