# ****
#  ****
#   ****
#    ****
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print("")
#     if i != n - 1:
#         for k in range(i + 1):
#             print(" ", end="")
def pattern(n):
    for col in range(n):
        for _ in range(col):
            print(" ", end="")
        for _ in range(n):
            print("*", end="")
        print()


pattern(4)
