def lhs(a , b):
    sides = (a - b ) ** 2
    return sides


def rhs(a , b):
    sides = (a ** 2 ) - ( 2 * a * b ) + (b ** 2)
    return sides

print(" to prove (a-b)^2 = a^2 - 2ab + b^2, enter\n")
num1 = int(input('the value of a\n' ))
num2 = int(input('the value of b\n' ))

ls = lhs(num1 , num2)
rs = rhs(num1 , num2)

if ls==rs:
    print("the equation is true since lhs is {} and rhs is {} ".format(ls , rs ))

else:
    print("not equal")