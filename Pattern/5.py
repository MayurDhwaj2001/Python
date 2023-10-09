# *
# **
# ***
# ****

def pattern(n):
    for col in range(n):
        for _ in range(col+1):
            print("*", end="")
        print()


pattern(4)
