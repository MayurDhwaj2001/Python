from functools import reduce

num = [1, 3, 2, 4]

sum = reduce(lambda a, b: a + b, num)

print(sum)
