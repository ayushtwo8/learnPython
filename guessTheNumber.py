import random

predicted = False

generatedNum = random.randrange(1,10)
count = 0

gameName = "NUMBER GUESSING GAME"
print(gameName.center(30,'+'))
print("\n")

while predicted != True:
    count = count + 1
    predictedNum = int(input("Enter the number between 1 and 10: "))

    if(generatedNum == predictedNum):
        print(f"\nYou guessed it in {count} number of attempts.")
        predicted = True
    else:
        if (predictedNum > generatedNum):
            print("Try a lower number.")
        elif(predictedNum < generatedNum):
            print("Try a higher number.")    
        continue
        

print("Thank you!!")