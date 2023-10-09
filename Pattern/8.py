#    *
#   * *
#  *   *
# *******

def pattern(n):
    s = n
    p = 1
    for row in range(n):
        s -= 1
        for col in range(s):
            print(" ", end="")
        for top in range(p):
            print("*", end="")

        print()


pattern(4)
