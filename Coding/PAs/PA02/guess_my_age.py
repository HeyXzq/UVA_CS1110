# Jacquelyn(Ziqi) Xu gqj3wx

num = int(input("Pick a number between 1 and 10: "))
birthday = int(input("If you’ve already had a birthday this year, enter 1774. Otherwise, enter 1773: "))
birth_y = int(input("Enter the year that you were born: "))

magic_n = (num * 2 + 5) * 50 + birthday - birth_y
remainder = magic_n % 100

print('The magic number is "'+ str(magic_n) + '". That means you are ' + str(remainder) + '!')

