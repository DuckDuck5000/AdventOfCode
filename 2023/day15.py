D = open("input.txt").read().strip()
L = D.split('\n')


def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

steps = sequence.split(',')
D=D.split(',')
ans = 0
for step in D:
  ans += hash_algorithm(step)
print(ans, "part 1")

sequence = [
    "rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9",
    "ab=5", "pc-", "pc=6", "ot=7"
]


boxes = [[] for _ in range(256)]


def process_step(step):
    #print(boxes[:11])
    label, operation = step.split('=' if '=' in step else '-')
    box_number = hash_algorithm(label)
    #print(box_number)
    if operation == '':
        for i, lens in enumerate(boxes[box_number]):
            if lens.startswith(label):
                del boxes[box_number][i]
                break
    else:
        focal_length = int(operation)
        replaced = False
        for i, lens in enumerate(boxes[box_number]):
            if lens.startswith(label):
                boxes[box_number][i] = f"{label} {focal_length}"
                print(f"{label}{focal_length}")
                print(label+operation)
                replaced = True
                break
        if not replaced:
            boxes[box_number].append(f"{label} {focal_length}")


for step in D:
    process_step(step)


total_focusing_power = 0

for box_number, box in enumerate(boxes):
    for slot_number, lens in enumerate(box, start=1):
        label, focal_length = lens.split()
        focal_length = int(focal_length)
        focusing_power = (box_number + 1) * slot_number * focal_length
        total_focusing_power += focusing_power

print(total_focusing_power)

