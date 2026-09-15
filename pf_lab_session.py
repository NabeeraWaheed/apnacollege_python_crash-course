                                                    #LAB SESSION 1#

# Write a program for converting Degree Centigrade to Fahrenheit.
centigrade = float(input("Enter the value in Degree Centigrade: "))
fahrenheit = (centigrade * 9/5) + 32
print(centigrade, "Degree Centigrade is equal to", round(fahrenheit,2), "Degree Fahrenheit") 

# # Write a program for converting Degree Fahrenheit to Centigrade.
fahrenheit = float(input("Enter the value in Degree Fahrenheit: "))
centigrade1 = (fahrenheit - 32) * 5/9
centigrade = round(centigrade1,2)
print(fahrenheit, "Degree Fahrenheit is equal to", round(centigrade,2), "Degree Centigrade")

# # Write a program to calculate the area of rectangle.
length = float(input("Enter the value for length of rectangle: "))
width = float(input("Enter the value for width of rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

# # Write a program to calculate the volume of a sphere.
PI = 3.142
radius = float(input("Enter the value for radius of sphere: "))
volume1 = (4/3) * PI * radius ** 3
volume = round(volume1,2)
print("The volume of a sphere is", volume)

# # Write a program that can write your name is upper case, lower case, and title case.
name = input("Enter your name: ")
print("Your name in upper case is", name.upper())
print("Your name in lower case is", name.lower())
print("Your name in title case is", name.title())

# Calculate the compound interest by taking input from the user by using above formula.
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time span in years: "))
A = P * (1 + R / 100) ** T
compound_interest = A - P
print("The compound interest is:", round(compound_interest, 2))


                                                 #LAB SESSION 2#

#Program 1: Practicing with math operators
# a = 10
# b = 22
# print("Sum is:", a+b)
# print("Difference is:", a-b)
# print("Product is:", a*b)
# print("Division is:", a/b)
# print("Integer Division is:", a//b)
# print("Raised to the Power is:", a**b)
# print("Remainder is:", a%b)

#Program 2: Write a program to use assignment operators
#x = 5
#x += 3 
#print(x)
#x -= 3 
#print(x)
#x *= 3 
#print(x)
#x /= 3 
#print(x)
#x %= 3 
#print(x)
#x //= 3 
#print(x)
#x **= 3 
#print(x)
#x &= 3 
#print(x)
#x |= 3 
#print(x)
#x ^= 3 
#print(x)
#x >>= 3 
#print(x)
#x <<= 3 
#print(x)

#Program 3: Write a program to perform comparison operators.
# x = 20
# y = 15
# print("x is equal to y:", x == y)
# print("x is not equal to y:", x != y)
# print("x is greater than y:", x > y)
# print("x is less than y:", x < y)
# print("x is greater than or equal to y:", x >= y)
# print("x is less than or equal to y:", x <= y)

#Program 4: Write a program to perform logical operators.
# x = 15
# print(x > 13 and x < 20)
# x = 25
# print(x > 23 or x < 24)
# x = 35
# print(not(x > 33 and x < 40))

#Program 5: Write a program to perform identity operator.
# x = ["ahmed", "bashir"]
# y = ["ahmed", "bashir"]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)

#Program 6: Performing is not identity operation.
# x = ["ahmed", "bashir"]
# y = ["ahmed", "bashir"]
# z = x
# print(x is not z)
# print(x is not y)
# print(x != y)

#Program 7: Performing 'in' membership operation.
# x = ["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
# print("faisal" in x)

#Program 8: Performing 'not in' membership operation.
# x = ["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
# print("parkash" not in x)

#Program 9:  You are planning to throw a small bird at a distance d, with time t, and height h to some structure. 
#Write a code in which you will use the physical quantities such as initial velocity, final velocity, angle in radians, gravity, height, sling shot etc
#import math
# velocity = float(input('Give me a velocity to fire at (in m/s): '))
# angle = float(input('Give me an angle to fire at: '))
# distance = float(input('Give me how far away you are from the structure: '))
# height = float(input('Give me the height of the structure (in meters): ')) 
# slingshot = 5 
# gravity = 9.8 
# angleRad = math.radians(angle)
# x = math.cos(angleRad)
# y = math.sin(angleRad)
# time = distance/(velocity * x)
# vx = x
# vy = y + (-9.8 * time)
# finalVelocity = math.sqrt((vx ** 2) + (vy ** 2))

#Question 1. A ball at the end of a string is revolving uniformly in a horizontal circle of radius 2 meters at constant angular speed 10 rad/s.
#Determine the magnitude of the linear velocity of a point located:
# (a) 0.5 meters from the center
# (b) 1 meter from the center
# (c) 2 meters from the center
# Known: Radius (r) = 0.5 meters, 1 meter, 3 meters, The angular speed = 10 radians/second
# Wanted: The linear velocity
radius1 = 0.5
radius2 = 1
radius3 = 2
angular_speed = 10
linear_velocity1 = radius1 * angular_speed
linear_velocity2 = radius2 * angular_speed
linear_velocity3 = radius3 * angular_speed
print("The linear velocity of a point located 0.5 meters from the center is:", linear_velocity1, "m/s")
print("The linear velocity of a point located 1 meter from the center is:", linear_velocity2, "m/s")
print("The linear velocity of a point located 2 meters from the center is:", linear_velocity3, "m/s")

#Question 2. The blades in a blender rotate at a rate of 5000 rpm. Determine the magnitude of the linear velocity:
# (a) a point located 5 cm from the center (b) a point located 10 cm from the center Known: Radius (r) = 5 cm and 10 cm
# The angular speed (ω) = 5000 revolutions / 60 seconds = 83.3 revolutions / second = (83.3)(6.28 radian) /
# second = 523.3 radians / second
# Wanted: The magnitude of the linear velocity
r1 = 5
r2 = 10
angular_speed = 523.3
linear_velocity1 = r1 * angular_speed
linear_velocity2 = r2 * angular_speed
print("The linear velocity of a point located 5 cm from the center is:", round(linear_velocity1, 2), "cm/s")
print("The linear velocity of a point located 10 cm from the center is:", round(linear_velocity2, 2), "cm/s")

#Question  3. A  point  on  the  edge  of  a  wheel 30  cm in  radius, around  a  circle  at  constant  speed 10 meters/second.
# What is the magnitude of the angular velocity?
# Known: Radius (r) = 30 cm = 0.3 meters, The linear velocity (v) = 10 meters/second
# Wanted: the angular velocity
r = 0.3
v = 10
angular_velocity = v / r
print("The magnitude of the angular velocity is", round(angular_velocity, 2), "radians/second")

#Question 4. A car with tires 50 cm in diameter travels 10 meters in 1 second. What is the angular speed?
# Known:
# Radius (r) = 0.25 meter, The linear speed of a point on the edge of tires (v) = 10 meters/second
# Wanted: The angular speed
r = 0.25
v = 10
angular_speed = v / r
print("The angular speed is", round(angular_speed, 2), "radians/second")

#Question 5. The angular speed of wheel 20 cm in radians is 120 rpm. What is the distance if the car travels in 10 seconds.
# Known: Radius (r) = 20 cm = 0.2 meters
# The angular speed = 120 rev / 60 seconds = 2 rev / second = (2)(6.28) radians / second = 12.56 radians /
# second
# Wanted: distance
r = 0.2
angular_speed = 12.56
time = 10
distance = r * angular_speed * time
print("The distance the car travels in 10 seconds is", round(distance, 2), "meters")

#A car is running at a velocity of 50 miles per hour and the driver accelerates the car by 10 miles/hr2.
#How  far  the  car  travels  from  this  point  in  the  next  2  hours,  if  the  acceleration  is constant.
u = 50
a = 10
t = 2
s = (u * t) + (0.5 * a * t ** 2)
print("The distance the car travels in the next 2 hours is", round(s, 2), "miles")

#Question 7: A Stone is dropped freely from a height of 100 feet. With what velocity will it hit the ground?
#(Neglect     the    air     resistance     and    assume     the    acceleration     due    to    gravity    is    32ft/s2)
import math
h = 100
g = 32
u = 0
v = math.sqrt(2 * g * h)
print("The velocity with which the stone hits the ground is", round(v, 2), "ft/s")
