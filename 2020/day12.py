# open input.txt

file = open('input.txt', 'r') 

rawInput = [[x[0], int(x[1:])] for x in file.read().splitlines()]

# Class for both parts.
class Ship():
    def __init__(self):
        self.facing = 'E'
        self.coord_x = 0
        self.coord_y = 0
        # Relatives to ship coords x y.
        self.wayp_x = 10
        self.wayp_y = 1
 
    def move(self, direction, number):
        """
        Moves the ship {number} units in {direction}
        """
        if direction == 'N':
            self.coord_y += number
        elif direction == 'S':
            self.coord_y -= number
        elif direction == 'E':
            self.coord_x += number
        elif direction == 'W':
            self.coord_x -= number
    
    def move_waypoint(self, direction, number):
        """
        Moves the waypoint {number} units in {direction}
        """
        if direction == 'N':
            self.wayp_y += number
        elif direction == 'S':
            self.wayp_y -= number
        elif direction == 'E':
            self.wayp_x += number
        elif direction == 'W':
            self.wayp_x -= number
    
    def rotate(self, turn, amount):
        """
        Rotates the ship in {turn} direction {amount} degrees
        """
        to_angles = {'N': 90, 'S': 270, 'E': 0, 'W': 180}
        to_facing = {90: 'N', 270: 'S', 0: 'E', 180: 'W'}
        if turn == 'R':
            angle = (to_angles[self.facing] - amount) % 360
            self.facing = to_facing[angle]
        elif turn == 'L':
            angle = (to_angles[self.facing] + amount) % 360
            self.facing = to_facing[angle]
    
    def rotate_waypoint(self, turn, amount):
        """
        Rotates the waypoint around the ship
        in {turn} direction {amount} degrees
        """
        if turn == 'R':
            angle = 360 - amount
        elif turn == 'L':
            angle = amount
 
        if angle == 90:
            helper = self.wayp_x
            self.wayp_x = -1 * self.wayp_y
            self.wayp_y = +1 * helper
        elif angle == 180:
            self.wayp_x = -1 * self.wayp_x
            self.wayp_y = -1 * self.wayp_y
        elif angle == 270:
            helper = self.wayp_x
            self.wayp_x = +1 * self.wayp_y
            self.wayp_y = -1 * helper
 
    def move_ship_to_wayp(self, number):
        self.coord_x += number * self.wayp_x
        self.coord_y += number * self.wayp_y
 
# Part one.
my_ship = Ship()
for order in rawInput:
    action = order[0]
    value = order[1]
    if action == 'F':
        my_ship.move(my_ship.facing, value)
    elif action in ['R', 'L']:
        my_ship.rotate(action, value)
    elif action in ['N', 'S', 'E', 'W']:
            my_ship.move(action, value)

answer_1 = abs(my_ship.coord_x) + abs(my_ship.coord_y)
print(f"Part 1 - Manhattan Dist: {answer_1}")
 
# Part two.
my_ship_2 = Ship()
for order in rawInput:
    action = order[0]
    value = order[1]
    if action == 'F':
        my_ship_2.move_ship_to_wayp(value)
    elif action in ['R', 'L']:
        my_ship_2.rotate_waypoint(action, value)
    elif action in ['N', 'S', 'E', 'W']:
            my_ship_2.move_waypoint(action, value)
answer_2 = abs(my_ship_2.coord_x) + abs(my_ship_2.coord_y)
print(f"Part 2 - Manhattan Dist: {answer_2}")
