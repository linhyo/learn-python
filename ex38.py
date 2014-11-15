ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

'''
Adding:  Boy
There are 7 items now.
Adding:  Girl
There are 8 items now.
Adding:  Banana
There are 9 items now.
Adding:  Corn
There are 10 items now.
'''

print "There we go: ", stuff
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print "Let's do some things with stuff."

print stuff[1]
# Oranges
print stuff[-1] # whoa! fancy
# Corn
print stuff.pop()
# Corn
print ' '.join(stuff) # what? cool!
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print '#'.join(stuff[3:5]) # super stellar!
# Telephone#Light
