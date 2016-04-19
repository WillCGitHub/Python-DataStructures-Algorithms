"""
Bubble Sort 
"""

def swap(arr, e1, e2):
	temp = arr[e2]
	arr[e2] = arr[e1]
	arr[e1] = temp
	return arr

def BubbleSort (arr):
	counter = 0
	for outer in range (0, len(arr)-1):
		counter+=1
		for idx in range(0,len(arr)-counter):
			if arr[idx] > arr[idx+1]:
				swap(arr,idx,idx+1)
	return arr
			




numbers = ['apple','best','bubble','element','ace','awesome']
print (BubbleSort(numbers))