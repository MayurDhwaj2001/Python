# ****
# *  *
# *  *
# ****

def pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == n - 1 or i == n - 1 or j == 0:
                print("", end="*")
            else:
                print(" ", end="")
        print("\n", end="")


pattern(4)
