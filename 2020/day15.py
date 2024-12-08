

rawInput = [6,3,15,13,1,0]
visitedMap = {}
penul = {}
turns = 30000000, 2020
turn = 0
## initialize map

for index, num in enumerate(rawInput):
    visitedMap[num] = [index+1]
    turn += 1
 
last = rawInput[-1]

while True:
    
    turn += 1
    if turn == turns +1:
        break
    ## First time we have seen the number
    if len(visitedMap[last]) == 1:
        visitedMap[0] = [visitedMap[0][-1], turn]
        
        last = 0
            # if num has been spoken before
    else:
            # calculate difference between last spoken turn and current turn
        diff = visitedMap[last][-1] - visitedMap[last][0]
            # if diff value not in dict add it
        if diff not in visitedMap:
            visitedMap[diff] = [turn]
            # else update list for spoken num
        else:
            visitedMap[diff] = [visitedMap[diff][-1], turn]
        last = diff

print(last)



### Code that didn't time out

def memory_game(numbers, final_turn):
	turn_spoken = {num: i + 1 for i, num in enumerate(numbers[:-1])}

	next_num = numbers[-1]
	for turn_num in range(len(numbers)+1, final_turn+1):
		last_turn_num = turn_num - 1
		if next_num in turn_spoken:
			spoken_num = last_turn_num - turn_spoken[next_num]
		else:
			spoken_num = 0
		turn_spoken[next_num] = last_turn_num

		next_num = spoken_num
	
	return spoken_num

with open("input.txt", "r") as file:
	numbers = [int(num) for num in file.read().split(",")]

# Part 1
print("Part 1:", memory_game(numbers, 2020))

# Part 2
print("Part 2:", memory_game(numbers, 30000000))
