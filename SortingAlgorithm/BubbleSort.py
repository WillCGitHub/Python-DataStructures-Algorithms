"""
Bubble Sort 
Time Complexity: O(n), Average O(n^2) 
"""
class BubbleSort():
	def __init__(self):
		pass
	def swap(self,arr, e1, e2):
		temp = arr[e2]
		arr[e2] = arr[e1]
		arr[e1] = temp
		return arr

	def BubbleSort (self,arr):
		if arr is None:
			print ("The array is none")
			return arr
		counter = 0
		for outer in range (0, len(arr)-1):
			counter+=1
			for idx in range(0,len(arr)-counter):
				if arr[idx] > arr[idx+1]:
					self.swap(arr,idx,idx+1)
		return arr
			


if __name__ == '__main__':
	numbers = ['apple','best','bubble','element','ace','awesome']
	a = BubbleSort()
	print(a.BubbleSort(numbers))