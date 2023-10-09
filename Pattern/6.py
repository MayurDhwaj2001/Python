#    *
#   **
#  ***
# ****

def pattern(n):
    m = n
    s = 1
    for col in range(n):
        m -= 1
        for _ in range(m):
            print(" ", end="")
        for _ in range(s):
            print("*", end="")
        s += 1
        print()


pattern(4)
