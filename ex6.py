x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x	
#There are 10 types of people.
print y 
#Those who know binary and those who don't.

print "I said: %r." % x
#I said: 'There are 10 types of people.'.
print "I also said: '%s'." % y
#I also said: 'Those who know binary and those who don't.'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
#Isn't that joke so funny?! False

w = "This is the left side of..."
e = "a string with a right side."

print w + e
#This is the left side of...a string with a right side.
