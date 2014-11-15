name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
#Let's talk about Zed A. Shaw.
print "He's %d inches tall." % height
#He's 74 inches tall.
print "He's %d pounds heavy." % weight
#He's 180 pounds heavy.
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
#He's got Blue eyes and Brown hair.
print "His teeth are usually %s depending on the coffee." % teeth
#His teeth are usually White depending on the coffee.

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
#If I add 35, 74, and 180 I get 289.
