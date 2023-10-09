#    *
#   ***
#  *****
# *******

def pattern(n):
    m = n
    p = n
    plus2 = 1
    for row in range(n):
        p -= 1
        m += 1
        for _ in range(p):
            print(" ", end="")
        for _ in range(0, plus2):
            print("*", end="")
        plus2 = plus2 + 2
        print()


pattern(4)
