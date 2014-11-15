print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
'''You'd need to know 'bout escapes with \ that do
 newlines and   tabs.
'''

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"
'''
--------------

       The lovely world
with logic so firmly planted
cannot discern
 the needs of love
nor comprehend passion from intuition
and requires an explanation

              where there is none.

--------------
'''

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# This should be five: 5

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# With a starting point of: 10000
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# We'd have 5000000 beans, 5000 jars, and 50 crates.

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
# We'd have 500000 beans, 500 jars, and 5 crates.
