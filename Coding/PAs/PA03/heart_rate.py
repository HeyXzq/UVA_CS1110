# Jacquelyn Xu gqj3wx
import random
# gellish2
def gellish2(age_min=1, age_max=100):
    global hrmax
    age = random.randint(age_min, age_max)
    hrmax = float(191.5 - (0.007 * (age ** 2)))
    return hrmax

# in target range
def in_target_range(hr,	age_min=1, age_max=100):
    a = gellish2(age_min, age_max)
    c = (hr <= 0.85 * a and hr >= 0.65 * a)
    return c



