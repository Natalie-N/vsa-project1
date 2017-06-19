# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

print "Hello World"


name = raw_input("Enter Your Name: ")
#print name
age = raw_input('Enter your Age: ')
#print age

age_int = int(age)

if age_int > 100:
    h = age_int - 100
    hh= 2017 - h
    print name, "turned 100", h, "years ago. That was year", hh, ". You can watch whatever movie you want."
    print "*claps*"

bday = raw_input("Have you had a birthday this year? ")
if bday == 'yes':
    x = 99 - age_int
    z = 2017 + x
    #print x
    print "cool"
    print name, " will be 100 in", x, "years. That is year", z, "."

else:
    y = 100 - age_int
    zz = 2017 + y
    print name, " will be 100 in", y, "years. That's year", zz, "."
        #print y
    print "also cool"


if age_int < 13:
    parents = raw_input("Are your parents with you when watching the movie?")

    if parents == 'yes':
        print "You are only allowed to watch G or PG movies."
    elif parents == 'no':
        print "You can only watch G rated movies. heh."

if age_int >= 13:
    #print "that's nice"
    if age_int < 17:
        print "You can watch G, PG, or PG13 movies."
    if age_int >= 17:
        print "You can watch G, PG, PG13, or R rated movies."

























