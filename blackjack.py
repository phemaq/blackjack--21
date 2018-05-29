koloda = [6,7,8,9,10,2,3,4,11] * 4

import random
random.shuffle(koloda)

print('play in a point?')
count = 0

while True:
      choice = input('Will you take a card? y/n\n')
      if choice == 'y':
          current = koloda.pop()
          print ('You got a dignity card %d'  %current)
          count += current
        if count > 21:
            print('Sorry, you lose)
                  break
                elif count == 21:
                  print('Congratulations, you scored 21!')
                      break
                  else:
                  print('You have %d points.' %count)
                elif choice == 'n':
                  print('You have %d points and you have finished the game.' %count)
                  break
        print('See you later!')
