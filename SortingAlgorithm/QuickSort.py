"""
Implementing the sorting algorithm, quick sort. 

quickSort method implements the 2 partitions common quick sort. 
quickSort(list)



quickSort3Way method implements the 3 partitions quick sort, specifically designed for data that has many duplicates. 
(Bentley-McIlroy 3-way partitioning)

quickSort3Way()
"""

class QuickSort():
	def __init__(self):
		pass
	def swap(self,arr,e1,e2):
		temp = arr[e1]
		arr[e1] = arr[e2]
		arr[e2] = temp
		return arr

	def quickSort(self,arr):
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
			partition1 = self.quickSort(partition1)
		if len(partition2) > 1:
			partition2 = self.quickSort(partition2)
		newArr = partition1+[pivot]+partition2


		return newArr


	def quickSort3Way(self,arr):
		if arr is None:
			return arr 
		elif len(arr) ==1:
			return arr
		elif len(arr) == 2:
			if arr[0] > arr[1]:
				self.swap(arr,0,1)
				return arr
			else:
				return arr


		elif len(arr)>2:
			pivot = arr[0]
			#print ("pivot is {}".format(pivot))
			i = 1
			j = len(arr)-1
			p = 1 
			q = len(arr)-1
			partition_sl = []
			partition_eq = []
			partition_gt = []
			#phase 1 scan from left to right 
			#and right to left
			#5 parts 
			#equal, smaller than, unkown, greater than, equal
			while(1):
				while (arr[i] < pivot):
					if i >= len(arr)-1:
						break
					i+=1

				while (arr[j]>pivot):
					if j <= 1:
						break
					j-=1
				
				if j > i:
					arr = self.swap(arr,i,j)
				else:
					if (j == i) and (i != len(arr)-1):
						j-=1
						break
					elif (j == i) and (i == len(arr)-1):
						break
					else:
						break

				if arr[i] == pivot:
					arr = self.swap(arr,i,p)
					p+=1
					if i <len(arr)-1:
						i+=1


				if arr[j] == pivot:
					arr = self.swap(arr,j,q)
					q-=1		

			#phase 2 swap equal partition to the middle
			#smaller than, equal, greater than

			while (p > 0) and (p <= j):
				p-=1
				arr = self.swap(arr,p,j)
				j-=1

			while (q<len(arr)-1) and (q >=i):
				q+=1
				arr = self.swap(arr,q,i)
				i+=1

			if j == i :
				for ele in arr[:j]:
					partition_sl.append(ele)
				for ele in arr[j+1:i]:
					partition_eq.append(ele)
				for ele in arr[i:len(arr)]:
					partition_gt.append(ele)
			else:
				for ele in arr[:j+1]:
					partition_sl.append(ele)
				for ele in arr[j+1:i]:
					partition_eq.append(ele)
				for ele in arr[i:len(arr)]:
					partition_gt.append(ele)

			if len(partition_sl) > 1:
				partition_sl = self.quickSort3Way(partition_sl)
			if len(partition_gt) > 1:
				partition_gt = self.quickSort3Way(partition_gt)
			

			newArr = partition_sl+partition_eq+partition_gt
			return newArr




if __name__ == '__main__':

	#numbers = [13,9,36,9,8,6,4,2,9,5,10,9,9,20,35,3,12,13,5,6,9,9,9]
	#numbers = [6,9,16,19,24,35,44,14,17,23,31,45,22,49,55,29,38,50,54,59]
	numbers = [1,3,4,6,8,2,5,7,9,24,25,28,30,23,27,32,59,64,65,92,95,103,60,63,93,97,99,98,31,33]
	#numbers = [54, 49, 45, 50]
	print (len(numbers))
	a = QuickSort()
	sortedArr = a.quickSort3Way(numbers)
	normalsort = a.quickSort(numbers)
	print (sortedArr)
	print (normalsort)


