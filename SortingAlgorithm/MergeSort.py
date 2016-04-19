"""
Merge Sort
Worst case complexity is O(nlogn)

To use merge sort, one needs to instantiate a class

a = [1,3,2,4,6,3,5]
b = MergeSort()
b.MergeSort(a)
"""
import BubbleSort

class MergeSort():
	def __init__(self):
		pass

	def  MergeSort(self,arr):
		newList = []
		p = 0
		r = len(arr)-1
		q = int((p+r)/2)

		partition1 = arr[0:q+1]
		partition2 = arr[q+1:len(arr)]
		if (len(partition1)>1):
			partition1 = self.MergeSort(partition1)
		if (len(partition2)>1):
			partition2 = self.MergeSort(partition2)
		
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
	a = [1,10,5,8,66,30,59,102,33,60,99,1002,88,66,33,22,11,88,669,30]
	merge = MergeSort()
	bubble = BubbleSort.BubbleSort()
	b = merge.MergeSort(a)
	c = bubble.BubbleSort(a)
	if b == c:
		print (True)

