import heapq
from collections import defaultdict

def process_file(filename):
    heap1, heap2 = [], []
    total_distance = 0
    freqMap = defaultdict(int)
    nums = []
    final_num = 0

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                parts = line.strip().split()
                
                if len(parts) == 2:
                    heapq.heappush(heap1, int(parts[0]))
                    heapq.heappush(heap2, int(parts[1]))
                    
                    freqMap[int(parts[1])] += 1
                    nums.append(int(parts[0]))
                else:
                    print(f"Skipping invalid line: {line}")
            # Part 1
            while heap1 and heap2:
                total_distance += abs(heapq.heappop(heap1) - heapq.heappop(heap2))
            
            # Part 2
            for num in nums:
                if num in freqMap:
                    final_num += num * freqMap[num]
            
            return total_distance, final_num

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None
    except ValueError as e:
        print(f"Error converting to integer: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

# Usage
filename = 'input_day1.txt'
distance, final = process_file(filename)

if distance is not None and final is not None:
    print(f"Part 1: Total Distance: {distance}")
    print(f"Part 2: Final Number: {final}")