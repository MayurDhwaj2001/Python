class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):  # <---- define iteration
        return self

    def __next__(self):  # <----- To get next value
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val

        else:
            raise StopIteration  # <----- Stop Iteration


values = TopTen()
for i in values:
    print(i)

# OR
print("\n")

nums = [1, 2, 3, 5, 7, 4, 3, 5, 4]
it = iter(nums)
print(it.__next__())  # OR 👇
print(next(it))
