import random
print('Lets start the game by entering your name:')

name=input('Player 1, Please enter your name: ')

print('well player {} please guess a number that I have chosen '.format(name))

#random number pick function

def guessthenum():
    global rannum
    rannum=random.randint(0,20)
    try:
        global mynum
        mynum=int(input('Please enter a number that I have guessed between 0 and 20: '))
        if mynum==rannum:
            print('you have guessed right!! congrats!!')
        else:
            wrongnum()

    except ValueError:
        print('You did not enter a number. Please enter a number')



def wrongnum():
            try:
               while mynum!=rannum:

                    print(rannum)
                    newnum=int(input('guess again:'))
                    if newnum<rannum:
                        print('you guessed too low!!')

                    elif newnum>rannum:
                        print('you guessed too high!!')

                    else:
                        print('congrats! you got it')
                        break
                        

            except ValueError:
                    print('You did not enter a number. Please enter a number')
                
guessthenum()
                
