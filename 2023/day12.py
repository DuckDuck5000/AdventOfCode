def read_grid(file_path):
    with open(file_path, "r") as file:
        return [(line.strip().split()[0], list(map(int, line.strip().split()[1].split(',')))) for line in file]

def count_configurations(dots, blocks, position=0, block_index=0, current_block_length=0, memo=None):
    if memo is None:
        memo = {}
    
    key = (position, block_index, current_block_length)
    if key in memo:
        return memo[key]
    
    if position == len(dots):
        return int(block_index == len(blocks) and current_block_length == 0)
    
    count = 0
    for char in ['.', '#']:
        if dots[position] == char or dots[position] == '?':
            if char == '.':
                if current_block_length == 0:
                    count += count_configurations(dots, blocks, position + 1, block_index, 0, memo)
                elif block_index < len(blocks) and blocks[block_index] == current_block_length:
                    count += count_configurations(dots, blocks, position + 1, block_index + 1, 0, memo)
            elif char == '#' and (block_index < len(blocks) and current_block_length < blocks[block_index]):
                count += count_configurations(dots, blocks, position + 1, block_index, current_block_length + 1, memo)
    
    memo[key] = count
    return count

def solve_puzzle(file_path, extend_grid=False):
    grid_data = read_grid(file_path)
    total_count = 0
    
    for dots, blocks in grid_data:
        if extend_grid:
            dots = '?'.join([dots] * 5)
            blocks = blocks * 5
        
        total_count += count_configurations(dots, blocks)
    
    return total_count

grid_file_path = "input.txt"
print(solve_puzzle(grid_file_path))

print(solve_puzzle(grid_file_path, extend_grid=True))
