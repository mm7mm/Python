import random
import string

# enter=input("Please type a sentence:")
# new_enter=""
# for i in enter:
#     if i not in string.punctuation:
#         new_enter+=i
# print("\n\n ****Here is the same sentnce without p unctuation****\n\n" ,new_enter)
num=[1,2,3,4,5,6,7,8,9,10]
print(random.choices(num,k=3))
st=random.choices(string.ascii_letters, k=10)
print(st)
