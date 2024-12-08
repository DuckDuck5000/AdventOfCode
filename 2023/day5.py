def parse_input(input_text):
  sections = input_text.split("\n\n")
  seeds = [int(x) for x in sections[0].split(":")[1].strip().split()]

  mapping_rules = []
  for section in sections[1:]:
      rules = []
      lines = section.split("\n")[1:] 
      for line in lines:
          numbers = [int(x) for x in line.split()]
          rules.append(tuple(numbers))
      mapping_rules.append(rules)

  return seeds, mapping_rules
def create_ranges(seed_ranges):
  seeds = []
  for i in range(0, len(seed_ranges), 2):
      start, length = seed_ranges[i], seed_ranges[i+1]
      seeds.extend(range(start, start + length))
  return seeds

def apply_mapping_rules(number, rules):
  for start_dest, start_src, length in rules:
      if start_src <= number < start_src + length:
          return start_dest + (number - start_src)
  return number

def apply_mapping_rules_to_range(start, length, rules):
  end = start + length
  for start_dest, start_src, length in rules:
      if start_src <= start < start_src + length:
        
          start = start_dest + (start - start_src)
          end = min(start_dest + length, start + (end - start))
          break
  return start, end-start

def find_lowest_location(seed_ranges, mapping_rules, p1=True):

  if p1:
    locations = []
    for seed in seeds:
      for rules in mapping_rules:
          seed = apply_mapping_rules(seed, rules)
      locations.append(seed)
    return min(locations)
  else:
    lowest_location = float('inf')
    for i in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[i], seed_ranges[i + 1]
        for rules in mapping_rules:
          start, length = apply_mapping_rules_to_range(start,   length, rules)
        lowest_location = min(lowest_location, start)
  
    return lowest_location
  return -1



seeds, mapping_rules = parse_input(input_text)
lowest_location = find_lowest_location(seeds, mapping_rules)
lowest_location_2 = find_lowest_location(seeds, mapping_rules, False)
print(lowest_location)
print(lowest_location_2)
