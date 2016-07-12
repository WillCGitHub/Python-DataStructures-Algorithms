"""
Merge Sort
Worst case complexity is O(nlogn)

To use merge sort, one needs to instantiate a class


"""

class MergeSort():
	def __init__(self, arr):
		self.arr = arr

	def MergeSort(self):
		return self.msort(self.arr)
	def msort(self,arr):
		newList = []
		p = 0
		r = len(arr)-1
		q = int((p+r)/2)

		partition1 = arr[0:q+1]
		partition2 = arr[q+1:len(arr)]
		if (len(partition1)>1):
			partition1 = self.msort(partition1)
		if (len(partition2)>1):
			partition2 = self.msort(partition2)
		
		newList = self.merge(partition1,partition2)
		return newList

	def merge(self,arr1,arr2):
		mergedList = []
		if (len(arr1)!=0) or (len(arr2) !=0):

			while (len(arr1) !=0) and (len(arr2)!=0):
				if arr1[0] == min(arr1[0],arr2[0]):
					mergedList.append(arr1.pop(0))
				elif arr2[0] == min(arr1[0],arr2[0]):
					mergedList.append(arr2.pop(0))
				elif arr1[0] == arr2[0]:
					mergedList.append(arr1.pop(0))
					mergedList.append(arr2.pop(0))
			if (len(arr1) == 0) and (len(arr2)!=0):
				for ele in arr2:
					mergedList.append(ele)
			elif (len(arr2) == 0) and (len(arr1)!=0):
				for ele in arr1:
					mergedList.append(ele)
			else:
				pass
			return mergedList
		else:
			return mergedList


if __name__ == '__main__':
	from random import randint
	numbers = []
	c = 0 # correct
	w = 0
	for idx in range(100):
		for idx in range(randint(0,100)):
			numbers.append(randint(0,1000))
		merge = MergeSort(numbers)
		msort = merge.MergeSort()
		answer = sorted(numbers)
		if msort == answer:
			c+=1
		else:
			w+=1
	print("100 test cases")
	print("{} passed".format(c))
	print("{} failed".format(w))

