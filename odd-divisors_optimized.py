#!/usr/bin/env python2.7

# the Odd number of Divisors problem
# Given 3 inputs A, B and K:
# where 1 < A < B 
# and K is a positive odd number.
# Implement the function evaluateDivisors(a,b,k) 
# The function should return the number of integers between A and B inclusive that have exactly K divisors.
###########################################################################################################

import math # import math for functions: sqrt, ceil, floor
import time # for timing funcitons


def iSquaredHasKDivisors(i, k):
	#return true if i has k divisors, else false
	count = 0
	perfect_sq = i * i
	step = 1;

	if perfect_sq % 2 != 0:
		step = 2 # if sq is odd we can skip even factors
	for divisor in range(1, i, step): # // loop from 1 to root of num (which is i).
		if perfect_sq % divisor == 0:
			count += 2
			if count > k:	
				return False


	""" code above is cleaner, using 'step' variable instead of writing loop twice
	if perfect_sq % 2 != 0: # if sq is odd we can skip even factors
		for divisor in range(1, i, 2):
			if perfect_sq % divisor == 0:
				count += 2
				if count > k:	
					return False
	else: # sq is even, gotta check all
		for divisor in range(1, i):
			if perfect_sq % divisor == 0:
				count += 2
				if count > k:	
					return False
	"""
	count += 1 # add one for the sqrt
	if count == k:
		return True
	return False

def evaluateDivisors(a, b, k):
	"""
	Returns number of ints from a to b inclusive that have exactly k divisors, where k is odd.
	The guarentee that k is odd allows us to make some optimizations and not have to iterate 
	over the entire range from a to b. The only case a number as an odd number of divisors is 
	if it's a perfect square, so two of it's roots are the same number. 

	This means we can just iterate over perfect squares from a to b. We do this by finding the 
	smallest and largest square root in the range and iterating over the roots themselves, 
	meaning we only ever look at perfect squares in range(a, b+1).

	checking if a prefect square n has a certain number of divisors is then a simple task, 
	dividing n by ints in range(1, sqrt(n)) and checking the remainder. 

	The process of finding divisors (by divison) is then simple and fast. 

	Further small optimisations can be made when checking if a perfect square n has k divisors, 
	such as not checking any even factors if the square is odd. 
	"""

	count = 0
	startSq = int(math.ceil(math.sqrt(a))) # find lowest sqrt in range
	endSq = int(math.floor(math.sqrt(b))) 	# find highest sqrt in range

	print("number of squares to check: ", endSq - startSq)
	for i in range((startSq), endSq + 1): # iterate through roots of perfect squares

		if iSquaredHasKDivisors(i, k):	# check this perfect square has k divisors
			count += 1

	return count

#--------------- TESTING FUNCITONS.---------------#

def testFunction(a, b, k, expect):
	""" tests a single set of inputs, returns true if output matches expected """
	print("testing your solution with inputs: A = {0}, B = {1}, k = {2}. range = {3}".format(a, b, k, b - a))

	#record system time to see how efficient the solution is
	start = time.time()
	retVal = evaluateDivisors(a, b, k)
	timeTaken = time.time() - start

	if retVal != expect:
		print("test failed, expected: {0}, actual output: {1}".format(expect, retVal))
		return False
	else:
		if timeTaken < 1:
			print("test succeeded in <1 second \n")
		else:
			print("test succeeded in", timeTaken, "seconds \n")

		return True


def testSuite():

	largeRanges = True # set this to true to test your solution against a larger range of numbers

	passed = 0
	numTests = 4
	
	print("running test suite")
	print("testing solution over a few small ranges")

	#test small ranges, see if coded properly
	if testFunction(4, 38, 3, 3):
		passed += 1
	if testFunction(2, 55, 5, 1):
		passed += 1
	if testFunction(42, 264, 9, 4):
		passed += 1
	if testFunction(114, 503, 15, 3):
		passed += 1

	if passed < 4 and largeRanges:
		print("failed to pass small ranges tests, won't attempt large ranges")
		largeRanges = False
	
	# now for larger ranges to test how optimized
	if largeRanges:
		numTests = 7
		if testFunction(1103, 26103, 21, 8):
			passed += 1
		if testFunction(1232, 1000001232, 9, 7807):
			passed += 1
		if testFunction(2543, 10000002543, 5, 61):
			passed += 1

	print("passed {0} out of {1} tests".format(passed, numTests))
	if passed == numTests:
		print("all tests passed successfully!")

testSuite() # actually run tests
