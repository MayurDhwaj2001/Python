a = 1


def something():
    global a  # <----------- This will allow to change the global variable
    a = 10
    print("Inside", a)


something()

print("Outside", a)
