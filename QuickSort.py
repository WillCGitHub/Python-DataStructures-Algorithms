def swap(arr,e1,e2):
	#print ("swap {} at index {} and {} at index {} ".format(arr[e1],e1,arr[e2],e2))
	temp = arr[e1]
	arr[e1] = arr[e2]
	arr[e2] = temp
	return arr

def quickSort(arr):
	pivot = arr[len(arr)-1]
	wall = 0
	partition1=[]
	partition2=[]
	for curr in range(0,len(arr)-1):
		
		if arr[curr] < pivot:
			arr = swap(arr,curr,wall)
			wall+=1
	
	for ele in arr[0:wall]:
		partition1.append(ele)
	for ele in arr[wall:len(arr)-1]:
		partition2.append(ele)

	if len(partition1) > 1:
		partition1 = quickSort(partition1)
	if len(partition2) > 1:
		partition2 = quickSort(partition2)
	newArr = partition1+[pivot]+partition2


	return newArr


def quickSort3Way(arr):
	pivot = arr[0]
	print ("pivot is {}".format(pivot))
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
			i+=1

		while (arr[j]>pivot):
			j-=1
		print ("j is {}".format(j))	
		print ("i is {}".format(i))
		print("i j swap")
		arr = swap(arr,i,j)
		print (arr)
		if arr[i] == pivot:
			arr = swap(arr,i,p)
			p+=1
			i+=1
			print("left equal pivot swap")
			print (arr)
		if arr[j] == pivot:
			arr = swap(arr,j,q)
			q-=1
			
			print("right equal pivot swap")
			print (arr)
		if j<i:
			break
	print (arr)
	print ("j is {}".format(j))	
	print ("i is {}".format(i))
	print ("p is {}".format(p))
	print ("q is {}".format(q))
	#phase 2 swap equal partition to the middle
	#smaller than, equal, greater than
	while (p >= 0) and (p <= j):
		p-=1
		arr = swap(arr,p,j)
		j-=1

	while (q<len(arr)-1) and (q >=i):
		q+=1
		arr = swap(arr,q,i)
		i+=1

	for ele in arr[:j+1]:
		partition_sl.append(ele)
	for ele in arr[j+1:i]:
		partition_eq.append(ele)
	for ele in arr[i:len(arr)]:
		partition_gt.append(ele)

	newArr = partition_sl+partition_eq+partition_gt
	print (partition_sl)
	print ("sl: {}, eq:{}, gt:{} ".format(len(partition_sl),len(partition_eq),len(partition_gt)))
	return newArr






#numbers = [13,9,36,9,8,6,4,2,9,5,10,9,9,20,35,3,12,13,5,6,9,9,9]
numbers = [3,99,5,7,9,3,0,3,6,90,9,1,3,9,3,8,6,3]
#numbers = [2,3,5,9,10]
print (len(numbers))
sortedArr = quickSort3Way(numbers)
print (len(sortedArr))
print (sortedArr)



