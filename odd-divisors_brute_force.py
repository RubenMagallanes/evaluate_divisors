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


def iHasKdivisors(i, k):
	#return true if i has k divisors
	divs = 0

	for fact in range(1, i+1):
		if i % fact == 0:
			divs += 1

	if divs == k:
		return True
	return False


#return number of ints from a to b inclusive that have exactly k divisors, where K IS ODD 
def evaluateDivisors(a, b, k):
	count = 0
	for i in range(a, b+1):
		if iHasKdivisors(i, k):
			count += 1

	return count




#--------------- TESTING FUNCITONS.---------------#

def testFunction(a, b, k, expect):
	""" tests a single set of inputs, returns true if output matches expected """
	print("testing your solution with inputs: A = {0}, B = {1}, k = {2}".format(a, b, k))
	print("range =", b - a)

	#record system time to see how efficient the solution is
	start = time.time()
	retVal = evaluateDivisors(a, b, k)
	timeTaken = time.time() - start

	if retVal != expect:
		print("test failed, expected: {0}, actual output: {1}".format(expect, retVal))
		return False
	else:
		if timeTaken < 1:
			print("test succeeded in <1 second")
		else:
			print("test succeeded in", timeTaken, "seconds")

		return True


def testSuite():

	largeRanges = True#False # set this to true to test your solution against a larger range of numbers

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
