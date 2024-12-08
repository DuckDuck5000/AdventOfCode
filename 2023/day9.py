def extrapolate_next_value(history):
  sequences = [history]
  while True:
      differences = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
      sequences.append(differences)
      if all(diff == 0 for diff in differences):
          break

  next_value = sequences[-2][-1]
  for i in range(len(sequences) - 3, -1, -1):
      next_value += sequences[i][-1]

  return next_value

def extrapolate_previous_value(history):
  sequences = [history]
  while True:
      differences = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
      sequences.append(differences)
      if all(diff == 0 for diff in differences):
          break

  previous_value = sequences[-2][0]
  for i in range(len(sequences) - 3, -1, -1):
      previous_value = sequences[i][0] - previous_value

  return previous_value

def convert_to_integers(history_str):
  return [int(x) for x in history_str]

def read_file_and_calculate_sum(file_path, calculation_function):
  with open(file_path, 'r') as file:
      lines = [convert_to_integers(line.strip().split()) for line in file]
      return sum(calculation_function(history) for history in lines)

file_path = "input.txt"
sum_of_next_values = read_file_and_calculate_sum(file_path, extrapolate_next_value)
sum_of_previous_values = read_file_and_calculate_sum(file_path, extrapolate_previous_value)

print("Sum of Next Values:", sum_of_next_values)
print("Sum of Previous Values:", sum_of_previous_values)
