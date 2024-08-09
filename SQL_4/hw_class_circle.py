import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


# Examples:
circle = Circle(0, 0, 5)
point_inside = Point(2, 3)
point_outside = Point(6, 7)
point_on_border = Point(5, 0)
point_inside_near_border = Point(3, 3.9)

print(circle.contains(point_inside))  # True
print(circle.contains(point_outside))  # False
print(circle.contains(point_on_border))  # True
print(circle.contains(point_inside_near_border))  # True
