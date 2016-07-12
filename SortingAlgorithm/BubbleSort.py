"""
Bubble Sort 
Time Complexity: O(n), Average O(n^2) 
"""
class BubbleSort():
	def __init__(self,arr):
		self.arr = arr
	def swap(self,arr, e1, e2):
		temp = arr[e2]
		arr[e2] = arr[e1]
		arr[e1] = temp
		return arr

	def BubbleSort (self):
		arr = self.arr
		counter = 0
		for t in range(len(arr)):
			for idx in range(1,len(arr)):
				if arr[idx-1] > arr[idx]:
					self.swap(arr,idx-1,idx)
				if idx == len(arr)-counter-1:
					break
			counter+=1

		
		return arr
			


if __name__ == '__main__':
	from random import randint
	sample = []
	c = 0 #correct
	w = 0 #wrong
	for idx in range(100):
		for idx in range(randint(0,10)):
			sample.append(randint(0,100))
		bsort = BubbleSort(sample).BubbleSort()
		answer = sorted(sample)
		if bsort == answer:
			c+=1
		else:
			w+=1
	print("100 test cases")
	print("{} passed".format(c))
	print("{} failed".format(w))


	
