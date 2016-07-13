"""
Implementing the sorting algorithm, quick sort. 

quickSort method implements the 2 partitions common quick sort. 
quickSort(list)


quickSort3Way method implements the 3 partitions quick sort, 
specifically designed for data that has many duplicates. 

quickSort3Way()
"""

class QuickSort():
	def __init__(self,arr):
		self.arr = arr
	def swap(self,arr,e1,e2):
		temp = arr[e1]
		arr[e1] = arr[e2]
		arr[e2] = temp
		return arr

	def quickSort(self):
		return self._qs(self.arr)

	def _qs(self,arr):
		if len(arr) == 0 or len(arr) == 1:
			return arr
		pivot = arr[len(arr)-1]
		wall = 0
		partition1=[]
		partition2=[]
		for curr in range(0,len(arr)-1):
			
			if arr[curr] < pivot:
				arr = self.swap(arr,curr,wall)
				wall+=1
		
		for ele in arr[0:wall]:
			partition1.append(ele)
		for ele in arr[wall:len(arr)-1]:
			partition2.append(ele)

		if len(partition1) > 1:
			partition1 = self._qs(partition1)
		if len(partition2) > 1:
			partition2 = self._qs(partition2)
		newArr = partition1+[pivot]+partition2

		return newArr


	def quickSort3Way(self):
		return self._qs3(self.arr)

	def _qs3(self,arr):
		if len(arr)== 0 or len(arr) == 1:
			return arr 
		if len(arr) == 2:
			if arr[0] > arr[1]:
				self.swap(arr,0,1)
				return arr
			else:
				return arr

		lo = 0
		hi = len(arr)-1
		if arr[hi] <= arr[lo]:
			self.swap(arr,lo,hi)
		i = 1
		lt = 1
		gt = len(arr) -2
		while (1):
			if arr[i] < arr[lo]:
				self.swap(arr,i,lt)
				lt+=1
				i+=1
			elif arr[i] > arr[hi]:
				self.swap(arr,i,gt)
				gt-=1
			else:
				i+=1
			if i > gt:
				break

		lt-=1
		gt+=1
		self.swap(arr,lo,lt)
		self.swap(arr,hi,gt)

		partition_sl = arr[:lt]
		partition_md = arr[lt+1:gt]
		partition_gt = arr[gt+1:hi+1]

		if len(partition_sl) > 1:
			partition_sl = self._qs3(partition_sl)
		if len(partition_md) > 1:
			partition_md = self._qs3(partition_md)
		if len(partition_gt) > 1:
			partition_gt = self._qs3(partition_gt)

		newArr = partition_sl+[arr[lt]]+partition_md+[arr[gt]]+partition_gt
		return newArr




if __name__ == '__main__':
	from random import randint
	c = 0 #correct 
	w = 0 #wrong
	c3 = 0
	w3 = 0
	
	for outer_idx in range(1000):
		numbers = []
		for inner_idx in range(0,randint(0,100)):
			numbers.append(randint(0,1000))
		a = QuickSort(numbers)
		qsort3w = a.quickSort3Way()
		qsort = a.quickSort()
		answer = sorted(numbers)
		if qsort3w == answer:
			c3+=1
		else:
			w3+=1
		if qsort == answer:
			c+=1
		else:
			w+=1
	print('1000 test cases')
	print("Quick sort:\n{} passed , {} failed".format(c,w))
	print("Quick sort 3 ways:\n{} passed, {} failed".format(c3,w3))



