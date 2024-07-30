hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
words=["good","bad","ugly","var"]
x=6
random_word=random.choice(words)
display=["_"]*len(random_word)
print( ' '.join(display))
guessed_letters=[]
print(hangman[0])

while "_" in display  and x>0:
        guessed= input("Pleaseguess aletter: ").lower()
        if guessed in guessed_letters:
            print("You already guessed that. Try again.")
            print(f"You have {x} more tries")
            continue
        guessed_letters.append(guessed)
        if guessed not in random_word:
            x-=1
            print(hangman[6 - x])
        else:
            for i in range(len(random_word)):
                if random_word[i]==guessed:
                    display[i]= guessed
        print(' '.join(display))
        print(f"You have {x} more tries")
        
        print(display)
        print(f"You have {x} more")
if x==0:
    print("""
You lose!
""")
    print(hangman[-1])
else:
    print("""
                *************
                YOU WIN
                *************
                """)