#Ask user if the shape of the building is either square, rectangular or round
#Calculate area depending on the shape entered

shape = input("What is the shape of the building? (square, rectangular or round) ")

if shape == "square":
    square_length = float(input("Please enter length of the square building: "))
    print(f"The area of the building is {square_length ** 2}")
elif shape == "rectangular":
    rectangle_length = float(input("Please enter the length of the rectangular building: "))
    rectange_width = float(input("Please enter the width of the rectangular building: "))
    print(f"The area of the building is {rectangle_length * rectange_width}")
elif shape == "round":
    round_radius = float(input("Please enter the radius of the round building: "))
    import math
    print(f"The area of the building is {math.pi * round_radius * round_radius}")
