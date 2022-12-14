import sys
import random
import math
from time import time

class Point: 
    def __init__(self, x_init, y_init): 
        self.x = x_init 
        self.y = y_init 
    def get_x(self): 
        return self.x 
    def get_y(self): 
        return self.y 
    def __repr__(self): 
        return "".join(["(", str(self.x), ",", str(self.y), ")"]) 
    def __str__(self): 
        return "(%s,%s)" % (self.x, self.y) 
    def get_coord(self):
        coords = [self.x, self.y]
        return coords
    def distance(self, other):
        distance = math.sqrt((abs(self.x - other.x))**2 +(abs(self.y - other.y)**2))
        distance = round(distance, 2)
        data = [distance, (self.x, self.y), (other.x, other.y)]
        return data

distance_compare = []
runtime_compare = []

def findClosest(distance_objects):
    start_time = time()
    for index in range(len(distance_objects)):
        distance_compare.append(distance_objects[index][0])
    
    minimum = min(distance_compare)
    minimum_index = distance_compare.index(minimum)
    print(min(distance_compare))
    print("The answer is: ", distance_objects[minimum_index])
    end_time = time()
    runtime_compare.append(start_time - end_time)

# point_objects = []
distance_objects = []

while True:
    try:
        number_of_points = int(input("How many times do you want the loop to run?: "))
        max_value = int(input("Max Value of coordinates: "))
        for index in range(number_of_points):
            distance_objects.append(Point(random.randint(-max_value, max_value), 
            random.randint(-max_value, max_value)).distance(Point(random.randint(-max_value, max_value), 
            random.randint(-max_value, max_value))))
            # point_objects.append(Point(random.randint(-max_value, max_value), random.randint(-max_value, max_value)).get_coord())

        print(distance_objects)
        findClosest(distance_objects)
        distance_objects = []
        distance_compare = []
        
    except KeyboardInterrupt:
        sys.exit(0)