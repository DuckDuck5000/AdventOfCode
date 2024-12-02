def is_safe(levels):
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if not (1 <= diff <= 3 or -3 <= diff <= -1):
            return False
        if diff > 0:
            is_decreasing = False
        if diff < 0:
            is_increasing = False

    return is_increasing or is_decreasing


def count_safe_reports(data):
    reports = data.strip().split('\n')
    count_safe = 0

    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe(levels):
            count_safe += 1

    return count_safe


def count_safe_reports_with_dampener(data):
    reports = data.strip().split('\n')
    count_safe = 0

    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe(levels):
            count_safe += 1
            continue
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1:]
            if is_safe(modified_levels):
                count_safe += 1
                break

    return count_safe


# Example, copy and paste input into here haha
data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

part1_result = count_safe_reports(data)
part2_result = count_safe_reports_with_dampener(data)

print(f"Part 1: Number of safe reports: {part1_result}")
print(f"Part 2: Number of safe reports (with Problem Dampener): {part2_result}")
