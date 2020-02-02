#Pretty sure im done with the list building part of this one

thelist = []
incrementAdd = True
endNumber = True
#incrementvalue = 1

while(True):
	userinput = int(input(
"""Welcome to the ListMaker! Select an option:
1. CREATE: Write it out (Then why you using this script huh?)
2. CREATE: Autocreate
3. VIEW/EXPORT the List 
4. CLEAR the list
5. EXIT
Please enter (1,2,3,4 or 5): """))
	if (userinput == 1):
		print("Alright, enter the intergers you want in the list then enter 'done' to finish.")
		incrementvalue = 1 
		incremenType = 1
		addnum = ''
		while(True):
			try :
				addnum = input("Add a number: ")
				if addnum.lower() == 'done':
					break;
				thelist.append(int(addnum))
			except:
				print("Please enter a real number.")
		#break;
	elif(userinput == 2):
		while(True):
			incremenType = int(input(
"""How do you want to make your list?
1. Addition
2. Substraction
3. Multiplication
4. Division
Please enter (1,2,3 or 4): """))
			if (incremenType == 1 or incremenType == 2):
				incrementAdd = True
				break;
			elif (incremenType == 3 or incremenType == 4):
				incrementAdd = False
				break;
			else :
				print("Please enter a valid option.")

		while(True):
			try:
				userinput = int(input(
"""How do you want to build the list?
1. Provide an end number (will break till it is <= that number)
2. Provide a length.
Please enter (1 or 2): """))
				if (userinput == 1):
					endNumber = True
					break;
				elif (userinput == 2):
					endNumber = False
					break;
				else :
					print("Please enter a valid option.")
					break;
			except:
				print("Please enter a valid option.")

		while(True):
			try:
				incrementvalue = float(input("What is the incrementvalue?: "))
				startNumber = float(input("What will be your starting number?: "))
				break;
			except:
				print("Please enter a valid option.")

		if incremenType == 1:
			pass
		elif incremenType == 2:
			incrementvalue = incrementvalue*(-1)
		elif incremenType == 3:
			pass
		elif incremenType == 4:
			incrementvalue = 1/incrementvalue

		try:
			if (endNumber == True):
				endingNumer = float(input("Enter the ending number: "))
				thelist.append(startNumber)
				newnumber = startNumber

				while(True):
					if incremenType == 1 or incremenType == 3:
						if (incrementAdd): 
							newnumber = newnumber+incrementvalue
							if newnumber <= endingNumer:
								thelist.append(newnumber)
							else:
								break;
						else:
							newnumber = newnumber*incrementvalue
							if newnumber <= endingNumer:
								thelist.append(newnumber)
							else:
								break;
					if incremenType == 2 or incremenType == 4:
						if (incrementAdd): 
							newnumber = newnumber+incrementvalue
							if newnumber >= endingNumer:
								thelist.append(newnumber)
							else:
								break;
						else:
							newnumber = newnumber*incrementvalue
							if newnumber > endingNumer:
								thelist.append(newnumber)
							else:
								break;

			else :
				listLength = int(input("Enter the length of the list: "))
				thelist.append(startNumber)
				newnumber = startNumber

				while(len(thelist) < listLength):
					if incremenType == 1 or incremenType == 3:
						if (incrementAdd): 
							newnumber = newnumber+incrementvalue
							thelist.append(newnumber)
						else:
							newnumber = newnumber*incrementvalue
							thelist.append(newnumber)
					if incremenType == 2 or incremenType == 4:
						if (incrementAdd): 
							newnumber = newnumber+incrementvalue
							thelist.append(newnumber)
						else:
							newnumber = newnumber*incrementvalue
							thelist.append(newnumber)
		except:
			pass

	elif(userinput == 3):
		viewType = int(input(
"""How do you want to view the list?
1. View in the console
2. Export to a textfile
3. Export to a excel spreadsheet
4. Back
Please enter (1,2,3 or 4): """))
		if (viewType == 1):
			print(thelist)
		elif (viewType== 2):
			fileOpener = open("theList.txt","w")
			startNumber = thelist[0]
			endingNumer = thelist[-1:][0]
			fileOpener.write(str(startNumber)+" "+str(endingNumer)+" "+str(incrementvalue)+" "+str(incremenType)+"\n")
			for number in thelist:
				fileOpener.write(str(number)+"\n")
		elif (viewType == 3):
			print("can i do this without importing something? Under construction.")
		elif (viewType == 4):
			pass;
		else :
			print("Please enter a valid option.")

	elif(userinput == 4):
		thelist = []
		print("The list has been emptied.")

	elif(userinput == 5):
		print("Cya. Hopefully you can enjoy that list!")
		break;

	else :
		print("Please enter a valid option.")

'''
This is a script for making lists with missing numbers.
It will be used as the starting point for my first visualization project.

Ask the user how he/she wants to make the list; [done]
		1 - to manually input a list with missing numbers. - sort after entry. [done]
		2 - to auto create [done]
			a- get the increment type of the list (addition (negatives too) or multiplication (division too) have all 4 as seperate options tho) [done]
			b- get a starting number [done]
			c- get an ending number or length of list [done]
				if - the ending number doesnt make sense - loop back with while loop [done]*
				if - the ending numbers makes sense or a length is given [done]
					then - create the list [done]*
					ask the user if he/she wants to see the list or pick the missing number/numbers now or delete this list and make a new one or quit [done]
						if he/she wants to see the list [done]
							ask if he/she wants it to console or txt[done]
								output as desired and loop back [done]
						[CANCELLED]if he/she wants to pick a missing number/numbers or display the ones they already popped []
							ask which number should be removed or if he/she removed all she wanted []
								remove the number with pop (shifting all following indexes down one) []*
								loop back to the question []
'''