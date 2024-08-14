import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __contains__(self, point):
        return self.distance_to(point) <= self.radius


# Examples:
circle = Circle(0, 0, 5)
point_inside = Point(2, 3)
point_outside = Point(6, 7)
point_on_border = Point(5, 0)
point_inside_near_border = Point(3, 3.9)

print(point_inside in circle)  # True
print(point_outside in circle)  # False
print(point_on_border in circle)  # True
print(point_inside_near_border in circle)  # True

