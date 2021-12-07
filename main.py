import random

lower_bound = int(input("Enter a Lower Number"))
upper_bound =  int(input("Enter a Upper Bound Number"))

chances = 3
guess_number = random.randint(lower_bound, upper_bound)
count = chances

print("Your Number of Chances are:", chances)
try:
    for i in range(chances):
        number = int(input("Enter a Numebr to be guessed!"))

        if number == guess_number:
            print("Congratulation, you Guessed it Right!!!!")
            break
        else:
            print("Wrong Guess :)")
            count -= 1
            print("Remaining Chances are", count)
except:
    print("Error Occurs")