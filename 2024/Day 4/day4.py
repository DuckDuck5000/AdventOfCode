def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    total_count = 0

    
    directions = [
        (-1,  0),  
        (-1,  1),  
        ( 0,  1), 
        ( 1,  1), 
        ( 1,  0), 
        ( 1, -1),  
        ( 0, -1),  
        (-1, -1)   
    ]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                for w in [word, word[::-1]]:
                    nx, ny = x, y
                    match = True
                    for k in range(len(w)):
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if grid[nx][ny] != w[k]:
                                match = False
                                break
                            nx += dx
                            ny += dy
                        else:
                            match = False
                            break
                    if match:
                        total_count += 1
    return total_count


with open('C:\\Users\\<REDACTED>\\OneDrive\\Documents\\AdventOfCode\\2024\\input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
grid = [list(line) for line in lines]


word = "XMAS"

count = count_word_occurrences(grid, word)

print(f"The word '{word}' occurs {count//2} times in the grid.")


## part 2

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def check_diagonal(x, y, dx, dy):
        letters = []
        for k in range(-1, 2):  # Positions -1, 0, 1
            nx = x + k * dx
            ny = y + k * dy
            if 0 <= nx < rows and 0 <= ny < cols:
                letters.append(grid[nx][ny])
            else:
                return False 
        diag_word = ''.join(letters)
        if diag_word in ['MAS', 'SAM']:
            return True
        else:
            return False

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'A': 
                diag1 = check_diagonal(x, y, -1, -1)  
                diag2 = check_diagonal(x, y, -1, 1)   
                if diag1 and diag2:
                    count += 1
    return count

xmas_count = count_xmas(grid)
print(f"Number of X-MAS patterns: {xmas_count}")