import random
import time
#------------------
ball = ['Outlook not so good',
'A kangaroo is just a rabbit on steroids',
'I say yes',
"Reply is hazy",
'I say tomato you said potato',
'8ball thinks you funny',
'8ball says no',
'Fat like Nero, handsome like Commodus',
'Time flies so quickly',
'8ball is fond of you',
'Alexa, play "avicii"']







#--------------------------

def new_game():
    print('Hello')
    time.sleep(1)
    print('8ball is a magical friend')
    time.sleep(1.2)
    name =input('8ball wishes to know your name')
    time.sleep(0.5)
    input('what do you wish to know from 8ball today')
    print(random.choice(ball))
    time.sleep(0.2)
    print(name+' you have been blessed with  the wisdom of 8ball')
    print('Bye!!!')

new_game()
play = input('Do you want to play again')
if play.lower() == 'yes':
    new_game()
else:
    print('8ball will miss you')
      

