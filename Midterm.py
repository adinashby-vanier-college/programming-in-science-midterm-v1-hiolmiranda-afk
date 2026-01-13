import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * radius ** 2      

    return round(area, 2)
    

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n <= 3:
        return ("The triangle height should be at least 4.")
    
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end=" ")
            if col == 1 and row == n - 1:
                print(" ",end="")
    
    

# Q3: Inverted Pyramid

def inverted_pyramid(n):
    if n <= 2:
        return ("The pyramid should be at least 3.")

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()


def hollow_right_triangle(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end=" ")
            if col == 1 and row == 3:
                print(" ",end="")
           
        print()
print(hollow_right_triangle(4))

print(hollow_right_triangle(5))
print()

def inverted_pyramid(n):
    n = 3
    for row in range(n):
        for col in range(n):
            print("*", end=" ")
        spaces = row 
        stars = row 
        print(spaces * 2 + stars -1)

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
