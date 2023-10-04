def sum(a, b):
    sum = a + b
    print(sum)


sum(1, 2)


# Types of argument

# Position
def person(name, age):
    print(name, age)


person(name='mayur', age=22)


# Keyword
def person2(name, age):
    print(name, age)


person2(name='Dhwaj', age=20)


# Default
def person3(name, age=18):
    print(name, age)


person3('Dhwaj')


# Variable Length
def sub(subject, *marks):
    total = 0
    for i in marks:
        total=total+i
    print(subject,total)

sub('Class-10', 34, 56, 76, 32, 54)
