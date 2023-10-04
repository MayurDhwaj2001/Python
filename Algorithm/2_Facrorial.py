# 9!=1x2x3x4x5x6x7x8x9

def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i

    print(ans)


fact(9)


# Using Recursion


def rec(m):
    if m == 0:
        return 1

    return m * rec(m - 1)


ans = rec(5)
print(ans)
