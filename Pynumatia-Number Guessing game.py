import random
num = random.randint(1,20)

print('\x1b[36;1;6;86;243m' + 'SHOMILI DUARY - TASK (1)' + '\x1b[0m')

txt = "Let's play a NUMBER GUESSING game!"
text = txt.center(105)
print(text)

txt = "Guess a number between 1 to 20 and you will be getting 4 attempts!"
y = txt.center(105)
print(y)

guess1 = int(input("\nEnter your first guess : "))

if (guess1 != num):
    print("\nOops...it's an incorrect guess!")
    print("Better luck next time!")
    print("\nYour current score is 4/5.")
    
    if (guess1 > num):
        print('\x1b[34;1;6;86;243m' + "\nHint (2) : The number is smaller than your guessed number." + '\x1b[0m')
    else:
        print('\x1b[34;1;6;86;243m' + "\nHint (2) : The number is greater than your guessed number." + '\x1b[0m')
    
    guess2 = int(input("\nEnter your second guess : "))
    
    if (guess2 != num):
        print("\nSorry...it's an incorrect guess!")
        print("Try again!")
        print("\nYour current score is 3/5.")
        
        if (num % 2 == 0):
            print('\x1b[34;1;6;86;243m' + "\nHint (1) : It's an even number" + '\x1b[0m')
        else:
            print('\x1b[34;1;6;86;243m' + "\nHint (1) : It's an odd number" + '\x1b[0m')
        
        guess3 = int(input("\nEnter your third guess : "))  
        
        if (guess3 != num):
            print("\nIt's a wrong guess, better luck next time!")
            print("Your current score is 2/5.")
       
            if num > 1:
               for i in range(2, num // 2):
                   if(num % i) == 0:
                      print('\x1b[34;1;6;86;243m' + "\nHint (3) : It's not a prime number." + '\x1b[0m')
                      break
               else:
                   print('\x1b[34;1;6;86;243m' + "\nHint (3) : It's a prime number." + '\x1b[0m')
                   
            guess4 = int(input("\nEnter your fourth guess : "))   
            
            if (guess4 != num):
                print("\nI'm sorry...it's an incorrect guess!")
                print('\x1b[35;1;6;86;243m' + "\nNO WORRIES" + '\x1b[0m')
                print('\x1b[33;1;6;86;243m' + "So let me tell you the answer....\n" + '\x1b[0m')
                print('\x1b[36;1;6;86;243m' + 'SO',num, 'IS THE ANSWER' + '\x1b[0m')
                
            else:
                print('\x1b[33;1;6;86;243m' + "\nAmazing! You did it correct!" + '\x1b[0m')
                print('\x1b[36;1;6;86;243m' + "You scored 2/5!" + '\x1b[0m')
       
        else:
            print('\x1b[33;1;6;86;243m' + "\nGreat! You guessed the correct number!" + '\x1b[0m')
            print('\x1b[36;1;6;86;243m' + "You scored 3/5!" + '\x1b[0m')
        
    else:
        print('\x1b[33;1;6;86;243m' + "\nCongratulations! You guessed it right!" + '\x1b[0m')
        print('\x1b[36;1;6;86;243m' + "You scored 4/5!" + '\x1b[0m')
            
else:       
    print('\x1b[33;1;6;86;243m' + "\nCongratulations! You guessed it right!" + '\x1b[0m')
    print('\x1b[36;1;6;86;243m' + "You scored a PERFECT 5/5!" + '\x1b[0m')
