#    ****
#   ****
#  ****
# ****

def pattern(n):
    m = n
    for row in range(n):
        m -= 1
        for _ in range(m):
            print(" ", end="")
        for _ in range(n):
            print("*", end="")
        print()


pattern(4)
