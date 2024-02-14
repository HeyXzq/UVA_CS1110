
'''
a = 2
b = '!'
string_a = input(str("The result is: " + str(10/a) + "! Wohoo!"))
print(string_a, b)

a = 5
b = 17
x = a % b
print(x)
'''

'''
def npaa():
    name = "fluffy"
    place = "San Deigo"
    animal = "dog"
    age = "5"
    return name, place, animal, age

a, b, c, d = npaa()
print(a, b, c, d)
'''

'''
def some_function(input_value):
    x = input_value -2
    return x
x = 8
y = some_function(x)
print(x,y)

a = "cats"
b = 2
print(b+a)


# 2024.2.5
def add_stuff(a):
    x = a + 5
    return x
b = 4
print("Statement 1: The value of b is", b)
y = add_stuff(7)
print("Statement 2: The value of y is", y)
print("Statement 3: The value of b is", b)

number=int((input("Pick a number between 1 and 10: ")))
number=(number*2+5)*50
number_added=int(input("If you’ve already had a birthday this year, enter 1774. Otherwise, enter 1773: "))
number=(number+number_added)
born_year=int(input("Enter the year that you were born: "))
number=number-born_year
age=number%100
print("The magic number is “" +str(number)+ "”. That means you are " +str(age)+ "!")
#Zitai Ren, computing id: nnf8qq

def my_quiz(x, y = 2, z = 'word'):
    a = x * y
    return str(a) + z

print(my_quiz(y = 3, z = 'dog'))



def add_stuff(p):
    global c
    c = p + 5
    return c

d = add_stuff(10)

c = 4
c = c + 3
print(c)


def star_num(p, q):
    x = p ** q

z = star_num(3, 2)
print(z)
'''
