# Jacquelyn XU

'''
def coffee(cost, days):
    total = cost * days
    #reutrn(cost*days)
    return total

print(coffee(3, 100))

a = 3.21
b = 254
c = coffee(a, b)
print('The amount spent on coffee in a given year is $' + str(c))
'''

def coffee_2(cost, days):
    total = cost * days
    print('The amount spent on coffee in a given year is $' + str(total))
   # return total
z = coffee_2(3.21, 254)
print(z)
#这个是为什么会print出值，是不是因为function里面有print
