def can_form_target(target, numbers, part2 = False):
    def backtrack(index, current_value, part2 = False):

        if index == len(numbers):
            return current_value == target

        addition_result = backtrack(index + 1, current_value + numbers[index], part2)
        if addition_result:
            return True

        multiplication_result = backtrack(index + 1, current_value * numbers[index], part2)
        if multiplication_result:
            return True

        if part2:
            concat_val = int(str(current_value)+str(numbers[index]))
            or_operator_result = backtrack(index+1, concat_val, part2)
            if or_operator_result:
                return True

        return False

    if not numbers:
        return target == 0 
    return backtrack(1, numbers[0], part2) if len(numbers) > 0 else (target == 0)


def solve_equations(lines):
    total_sum = 0
    total_sum_2 = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        left, right = line.split(":")
        target = int(left.strip())
        nums = list(map(int, right.strip().split()))

        if len(nums) == 1:
            if nums[0] == target:
                total_sum += target
            continue

        if can_form_target(target, nums):
            total_sum += target
        if can_form_target(target, nums, True):
            total_sum_2 += target
        

    return total_sum, total_sum_2

## Solves Part 1 and 2
lines =  [line.strip() for line in  open('C:\\Users\\<REDACTED>\\OneDrive\\Documents\\AdventOfCode\\2024\\Day 7\\input.txt', 'r') if line.strip()]

result = solve_equations(lines)
print(result)  




