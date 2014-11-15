the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

'''
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
'''

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

'''
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
'''

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

'''
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
'''

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

'''
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
'''

print
print "Element list: %r" % elements
print

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

'''
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
'''
