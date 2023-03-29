# Name: Kyulim Kim
# SBUID: 115935868  

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):
 celcius = 5/9 * (int(fahrenheit)-32)
 print(celcius)
 return celcius

def what_to_wear(celsius):
   ans = int(celsius)
   if ans < -10:
       print("Puffy jacket")
   elif -10<ans<0:
       print("Scarf")
   elif 0<ans<10:
       print("Sweater")
   elif 10<ans<20:
       print("Light jacket")
   else:
       print("T-shit")

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    a = abs(((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2)
    return float(a)

def euclidean_distance(x1, y1, x2, y2):
    d = abs(((x2 - x1) + (y2 - y1))**(1/2))
    return float(d)

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = abs((((x2-x1)**2)+((y2-y1)**2))**(1/2))
    s2 = abs((((x3-x2)**2)+((y3-y2)**2))**(1/2))
    s3 = abs((((x3-x1)**2)+((y3-y1)**2))**(1/2))
    perimeter = s1+s2+s3
    return float(perimeter)

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 
import math

def deg2rad(deg):
    deg2rad = float(deg)*math.pi/180
    return float(deg2rad)

def apothem(number_sides, length_side):
   apothem = float(length_side)/(2*math.tan(deg2rad(180/float(number_sides))))
   return float(apothem)

def polygon_area(number_sides, length_side):
    polygon_area = float(number_sides)*float(length_side)*apothem(number_sides, length_side)/2
    return float(polygon_area)
    

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

