# import math

# class Line:
    
#     def __init__(self, coord1, coord2):
        
#         self.coord1 = coord1
#         self.coord2 = coord2

#     def distance(self):
#         x1, y1 = self.coord1
#         x2, y2 = self.coord2
#         return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#     def slope(self):
#         x1, y1 = self.coord1
#         x2, y2 = self.coord2
#         return ((y2 -y1)) / ((x2 - x1))


# coordinate1 = (3, 2)
# coordinate2 = (8, 10)

# li = Line(coordinate1, coordinate2)
# print(li.slope())
# print(li.distance())



# class Cylinder:

#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return 3.14 * self.radius ** 2 * self.height


#     def surface_area(self):
#         return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius ** 2)

# cil = Cylinder(2,3)
# print(cil.volume())
# print(cil.surface_area())


