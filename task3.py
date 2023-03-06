#Obtain swimming, cycling and running times
#Calculate the total time by doing a sum of these three
#Set conditions to establish if and what award is to be given

swimming = int(input("Please enter your swimming time in minutes: "))
cycling = int(input("Please enter your cycling time in minutes: "))
running = int(input("Please enter your running time in minutes: "))

total_time = swimming + cycling + running 

if total_time <= 100:
    print("Congratulations! You won the Provincial Colours award!")
elif total_time <= 105:
    print("Congratulations! You won the Provincial Half Colours award!")  
elif total_time <= 110:
    print("Congratulations! You won the Provincial Scroll award!")  
else:
    print("Sorry, you didn't qualify for an award.")  

