time_limits = [54, 81, 70, 88]
record_distances = [446, 1292, 1035, 1007]
def calc(time_limits, record_distances):
  total_ways = 1

  for time_limit, record_distance in zip(time_limits, record_distances):
      ways = 0
      for hold_time in range(0, time_limit + 1):
          travel_time = time_limit - hold_time
          distance = hold_time * travel_time
          if distance > record_distance:
              ways += 1
      total_ways *= ways

  return total_ways



# Calculate the result
result = calc(time_limits, record_distances)
print(result)


# part 2
times = [str(x) for x in time_limits]
dis = [str(x) for x in record_distances]
time = int("".join(times))
distance = int("".join(dis))


ways = 0
for hold_time in range(time + 1):
    travel_time = time - hold_time
    dist = hold_time * travel_time
    if dist > distance:
        ways += 1
print(ways)
