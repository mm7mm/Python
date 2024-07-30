import random
words=["good","bad","ugly","var"]
x=6
random_word=random.choice(words)
display=["_"]*len(random_word)
print(' '.join(display))
#اطلب تخمين حرف

while "_" in display  and x>0:
        guessed= input("Pleaseguess aletter: ").lower()
        if guessed not in random_word:
            x-=1
        for i in range(len(random_word)):
            if random_word[i]==guessed:
                display[i]= guessed
        print(display)
        print(f"You have {x} more")
if (x==0):
        print("""
**You Lose**
=========
  +-----+
  |     |
  O     |
 /|\    |
 / \    |
        |
=========

""")
else:      
    print("""
*************
   YOU WIN
*************
""")


        