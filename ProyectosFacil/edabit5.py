import math

#Stuttering Function
def stutter(word):
   return word[0:2]+"..."+word[0:2]+"..."+word

def solutions(a, b, c):  # A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x.
    # Given a, b and c, you should return the number of solutions to the equation.
    x = b * b - (4 * a * c)
    if x < 0:
        return 0
    elif x > 0:
        return 2
    else:
        return 1


def quadratic_equation(a, b, c):
    return ((b ** 2 - 4 * a * c) ** 0.5 - b) / 2 / a


print(quadratic_equation(1, 2, -3))  # should be 1
print(solutions(1, 0, -1))  # x² - 1 = 0 has two solutions (x = 1 and x = -1).
print(stutter("entregar"))