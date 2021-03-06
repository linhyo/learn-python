def add(a, b):
    print "ADDING %d + %d" % (a, b)
    # ADDING 30 + 5
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    # SUBTRACTING 78 - 4
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    # MULTIPLYING 90 * 2
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    # DIVIDING 100 / 2
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# Age: 35, Height: 74, Weight: 180, IQ: 50


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
"""
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391 Can you do it by hand?
"""
