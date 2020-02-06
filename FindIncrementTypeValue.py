filereader = open("theList.txt","r")
array1 = []

for line in filereader.readlines():
	if " " in line:
		listparameters = filereader.readline()
	elif line != "":
		array1.append(float(line.split('\n')[0]))

firstblock = array1[0:2]
secondblock = array1[2:4]
thirdblock = array1[4:6]

firstblock

print(firstblock)
print(secondblock)
print(thirdblock)

addition = []
substraction = []
multipication = []
division = []

def testblock(block):
	addition.append(block[1] - block [0])
	substraction.append(block[0] - block [1])
	multipication.append(block[1] / block [0])
	division.append(block[0] / block [1])

testblock(firstblock)
testblock(secondblock)
testblock(thirdblock)

print("add"+str(addition))
print("sub"+str(substraction))
print("mul"+str(multipication))
print("div"+str(division))

transformation = {"addition":addition, "substraction":substraction, "multipication":multipication, "division":division}

incrementvalue = 1
incremenType = 1

haspattern = False 

for transform in transformation:
	if transformation[transform] [0] == transformation[transform] [1] == transformation[transform] [2]:
		if transformation[transform] [0] >= 1:
			print("Predicting this list is made by "+transform + " with a value of "+ str(transformation[transform] [0]))
			incrementvalue = transformation[transform] [0]
			if transform == "addition":
				incremenType = 1
			elif transform == "substraction":
				incremenType = 2
			elif transform == "multipication":
				incremenType = 3
			elif transform == "division":
				incremenType = 4
			haspattern = True
			break;

if (haspattern):
	fileOpener = open("theList.txt","w")
	startNumber = array1[0]
	endingNumer = array1[-1:][0]
	fileOpener.write(str(startNumber)+" "+str(endingNumer)+" "+str(incrementvalue)+" "+str(incremenType)+"\n")
	for number in array1:
		fileOpener.write(str(number)+"\n")
else :
	print("Could not find a pattern in this list.")