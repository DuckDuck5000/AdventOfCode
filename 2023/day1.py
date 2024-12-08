import re

def sum_first_last_numbers(text, number_words=[]):
    digits = re.findall(r'\d', text)
    if digits:
        return int(digits[0] + digits[-1])
    for digit, word in enumerate(number_words, start=1):
        if word in text:
            text = text.replace(word, str(digit))

    numbers = re.findall(r'\d', text)
    return int(numbers[0] + numbers[-1]) if numbers else 0

with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

part1, part2 = 0, 0
for line in lines:
    part1 += sum_first_last_numbers(line)
    part2 += sum_first_last_numbers(line, number_words)

# Print the results
print(part1)
print(part2)
