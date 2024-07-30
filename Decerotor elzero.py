from time import time
def speedTest(func):
    def wrapper():
        start=time()
        func()
        end=time()
        print(f"Function Runing Time Is{end-start}")
    return wrapper
@speedTest
def bigloop():
    for number in range(1 ,30000):
        print(number)
bigloop()