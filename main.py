
import os,sys
import random
print("Hello....")
while True:
    print("Please Choose a game you want to play \n")
    print("1. Choose your own Adventure")
    print("2. Hangman")
    print("3. Rock Paper Scissors")
    print("4. Bubble shooter")
    print("5. Exit")
    n = input("Selected option : ")
    if n == "5":
        break    
    elif n == "1" :
        import choose_your_own_adventure as adv
        adv.fun()
    elif n == "2" :
        import Hangman as hm
        hm.hangman()
    elif n == "3" :
        import RockPaperScissors as rps
        rps.fun()
    elif n == "4" :
        import Bubble_Shooter as bs 
        bs.shoot()
    else:
        print("Please Select Correct option.....\n")
        
