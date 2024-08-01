import timeit

# Measure the time it takes to execute the expression "'Hello' * 2000"
print(timeit.timeit("'Hello' * 2000"))

name = 'Hi'
# Uncomment the line below to see how long it takes to repeat 'Hi' 1000 times
# print(name * 1000)

# Measure the time it takes to execute the expression "name = 'Hi' * 1000"
print(timeit.timeit("name = 'Hi' * 1000"))

# Measure the time it takes to generate a random integer between 1 and 1000 using random.randint()
# The setup imports the random module before executing the statement
print(timeit.timeit(stmt="random.randint(1, 1000)", setup="import random"))

# Repeat the timing of generating a random integer between 1 and 1000 four times
# The setup imports the random module before executing the statement
print(timeit.repeat(stmt="random.randint(1, 1000)", setup="import random", repeat=4))