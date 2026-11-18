#Write a program to define a class "2DPoint" with coordinates x and y as attributes. Create 
#relevant methods and print the objects. Also define a method distance to calculate the 
#distance between any two point objects. 



class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        d = ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
        return d

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Creating point objects
p1 = Point2D(3, 4)
p2 = Point2D(6, 8)

# Printing points
print("First Point:", p1)
print("Second Point:", p2)

# Calculating distance
print("Distance between points:", p1.distance(p2))