#EXERCISE, NUMBER GUESSING NAME
#Make a var, winning_number & assign any num to it.
#Ask user to guess a number.
#if user guess correctly then print "YOU Win !!!"
#if user didn't:
    #if user guessed lower than acctual print "too low"
    #if user guessed higher than actual print "too high"
#Bonus : how to generate random number in python

winning_number = 7
guessing_number = int(input("Guess the winning number: "))
if winning_number == guessing_number:
    print("YOU WIN!!!")
else:
    if guessing_number < winning_number:
        print("too low")
    else:
        print("too high")