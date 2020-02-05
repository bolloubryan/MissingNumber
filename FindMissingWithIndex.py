import math
filereader = open("theList.txt","r")
array1 = []

listparameters = filereader.readline()

listparameters = listparameters.split(" ")
startNumber = float(listparameters [0])
endingNumer = float(listparameters [1])
incrementvalue = float(listparameters [2])
incremenType = float(listparameters [3])

for line in filereader.readlines():
	if line != "":
		array1.append(float(line.split('\n')[0]))

#start + (incrementvalue * index)
#startNumber * index ^ incremenvalue

def findmissingindex (array):
	if array[0] == startNumber:
	#if array[0] == 1:
		low = 0
		if array[len(array)-1] == endingNumer:
			high = len(array)-1
			mid = math.ceil((high+low)/2)
			while (mid != high):
				if incremenType == 1 and array[mid] > (startNumber+(incrementvalue*mid)):
					high = mid
				elif incremenType == 2 and array[mid] < (startNumber+(incrementvalue*mid)):
					high = mid
				elif incremenType == 3 and array[mid] > (startNumber*(incrementvalue**mid)):
					high = mid
				elif incremenType == 4 and array[mid] < (startNumber*(incrementvalue**mid)):
					high = mid
				elif array[mid] == (startNumber+(incrementvalue*mid)):
					low = mid
				elif array[mid] == (startNumber*(incrementvalue**mid)):
					low = mid
				mid = math.ceil((high+low)/2)
			if incremenType == 1 or incremenType == 2:
				missing = (startNumber+(incrementvalue*mid))
			elif incremenType == 3 or incremenType == 4:
				missing = (startNumber*(incrementvalue**mid))
		else:
			missing = endingNumer
	else:
		missing = startNumber

	return missing

print("The missing number is "+str(findmissingindex(array1)))