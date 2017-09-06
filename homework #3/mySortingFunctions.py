# Name: Spencer Milbrandt
# Email: Spencer.Milbrandt@colorado.edu
# SUID: 102291821
#

import sys
import random
import time

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
	
	result=[]
	
	if len(lst) < 2:
		return lst
		
	else:
		
		mid = int(len(lst)/2)
		y = mergeSort(lst[:mid])
		z = mergeSort(lst[mid:])
		i = 0
		j = 0
		while i < len(y) and j < len(z):
				if y[i] > z[j]:
					result.append(z[j])
					j += 1
				else:
					result.append(y[i])
					i += 1
		result += y[i:]
		result += z[j:]
		return result

#------ Quick Sort --------------
def quickSort(lst):
   if lst == []: 
        return []
   else:
	   pivot = lst[0]
	   lesser = quickSort([x for x in lst[1:] if x < pivot])
	   greater = quickSort([x for x in lst[1:] if x >= pivot])
	   return lesser + [pivot] + greater
		   
		   
# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
	t0 = time.clock()
	sortFunction(lst)
	t1 = time.clock() # A rather crude way to time the process.
	return (t1 - t0)
	
	# Average/Worst Case Time Complexities for quickSort, mergeSort, and insertionSort
	if sortFunction == quickSort:
		print("Average Case:", (n(log(n)))) #Average Case for quickSort
		print("Worst Case:", (n^2)) #Worst Case for quickSort
	elif sortFunction == mergeSort:
		print("Average Case:", (n(log(n)))) #Average Case for mergeSort
		print("Worst Case:", (n(log(n)))) #Worst Case of mergeSort
	elif sortFunction == insertionSort:
		print("Average Case:", n^2) #Average Case for insertionSort
		print("Worst Case:", n^2) #Worst Case for insertionSort



