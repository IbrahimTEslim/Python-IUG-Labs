import cmath

a = input("Enter Your Quadratic Equation factors with in a correct way:(aX^2 + bx + c):\na: ");
if (a == 0):
    print"Error!! there must be a value for the quadratic factor (a)"
    exit()

b = input("b: ");
c = input("c: ");
x = b * b - 4 * a * c
if x == 0 or x > 0:
    first = (-b + cmath.sqrt(x)) / (2 * a)
    seconed = (-b - cmath.sqrt(x)) / (2 * a)
    print "\n\n", first, "\n", seconed
else:
    print "This Equation does not have a roots in Real Numbers Group !!", \
        "\none at least from it's roots is a " \
        "complex number (i) !! "
