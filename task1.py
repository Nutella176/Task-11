num1 = 67
num2 = 78
num3 = 34

#Compare num1 to num2 and print the larger value
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

#Determine if num1 is even or odd
if num1 % 2 == 0:
    print(f"{num1} is an even number")
else:
    print(f"{num1} is an odd number")

#Sort the numbers from largest to smallest     
if num1 > num2:
    if num1 > num3:
        print(num1, num3, num2)
    else:
        print(num3, num1, num2)
else:
    if num2 > num3:
        print(num2, num3, num1)
    else:
        print(num3, num2, num1)
