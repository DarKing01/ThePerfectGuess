from random import randint

randomNumber = int(randint(1, 99))

userNumber = -1

guesses = 1
while(userNumber != randomNumber):
    userNumber = int(input("Guess the number: "))
    if(userNumber > randomNumber):
        print("Lower number please")
        guesses +=1
    elif(userNumber < randomNumber):
        print("Higher number please")
        guesses +=1    

print(f"You guessed the number {randomNumber} in {guesses} attempts.")   
