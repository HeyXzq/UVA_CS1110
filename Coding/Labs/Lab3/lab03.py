# Jacquelyn Xu gqj3wx

personal_budget = 1500
def substract_from_budget(new_expenses):
    global personal_budget
    remaining_budget = personal_budget - new_expenses
    return remaining_budget

def divide_costs(required, optional = 1):
    # required: total cost of the bill -- rent + utilities
    # optional: amount of roommates or people you are splitting bill with
    return required / optional

def pay_bills():
    print("You currently have $" + str(personal_budget) + " left to spend this month. ")
    rent = float(input("How much did you spend on rent this month? "))
    utilities = float(input("How much did you spend on utilities this month? "))
    n_roommates = int(input("How many roommates do you have? "))
    food = float(input("How much did you spend on food/groceries this month? "))
    misc = float(input("How much did you spend on miscellaneous things this month? "))
    sum = food + misc + divide_costs(rent + utilities, n_roommates)
    b = substract_from_budget(sum)
    return b

c = pay_bills()
print("You now have $" + str(c) + " left to spend this month.")

# second
def c_to_f(t_in_c, wind_speed = 0):
    t_in_f = t_in_c * 9 / 5 + 32 - wind_speed * 0.7
    return t_in_f

print("The current temperate is: " + str(c_to_f(30, 10)) + " degrees fahrenheit.")
print("The current temperate is: " + str(c_to_f(20)) + " degrees fahrenheit.")

