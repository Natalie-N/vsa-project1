# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Yes or No: ")

#if birthday == "Yes":
    # Calculates the year that the user will be 100
    #y = str((99 - age) + 2017)
    #year= 2017

#else:

    #year = 2016


while age < 100:

     age = age + 1
     print age



#else:
    # Calculates the year that the user will be 100
    #y = str((100 - age) + 2017)

#print name, " will turn 100 in the year ", y, "."
