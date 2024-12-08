tempArray = rawInput.split("\n")

def adjustBounds(letter, low, high):

		if letter == "F" or letter== "L":
			high = low + (high - low) // 2
		elif letter == "B" or letter == "R":
			low = low + (high - low) //2 + 1
			
		return low, high
    

def partOne(array):
    
    seatId = 0
    seatList = []
    for line in array:
        rowLo, rowHi = 0, 127
        colLo, colHi = 0, 7
        
        for letter in line[:7]:
            rowLo, rowHi = adjustBounds(letter, rowLo, rowHi)
        
        for letter in line[7:]:
            colLo, colHi = adjustBounds(letter, colLo, colHi)
            
        # Part two shit
        seatList.append(rowLo*8+colLo)
        #print(seatList)
        
        ## Part 1 stuff
        ###seatId = max(seatId, rowLo*8 + colLo)
    ## return seatId <-- my answer for part 1
    seatList.sort()
    return seatList

def partTwo(seatList):
    
    firstSeat = seatList[0]
    for seat in seatList:
        if seat == firstSeat:
            firstSeat += 1
        else:
            return firstSeat

print(partOne(tempArray))
print(partTwo(partOne(tempArray)))
