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

index = 0
for number in array1:
	if incremenType == 1 or incremenType == 2:
		expected = startNumber+(incrementvalue*index)
		if expected == number:
			pass
		else :
			missing = expected
			break;
	if incremenType == 3 or incremenType == 4:
		expected = startNumber*(incrementvalue**index)
		if expected == number:
			pass
		else :
			missing = expected
			break;
	index += 1
print("The missing number is "+str(missing))