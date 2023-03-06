#Ask user to input a number
#Set conditions to see if number is divisable by 2 and 5
#Set conditions to see if number is divisable by 2 or 5
#Set conditions to see if number is not divisible by either 2 or 5
#Print results

number = int(input("Please enter a number: "))


if (number % 2 == 0) and (number % 5 == 0):
    print(f"{number} is divisible by 2 and 5, results are {number/2} and {number/5} respectively")
elif (number % 2 == 0 ) or (number % 5 == 0):
    print(f"{number} is either divisible by 2 or 5, results are {number/2} and {number/5} respectively")
else:
    print(f"{number} is not divisible by 2 or 5")
