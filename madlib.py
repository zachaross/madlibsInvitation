"""
This program takes in the user's information to create a unique story.  This
file was created by Mr. Ross
"""

print "Welcome my first program!"

personsName = raw_input("What is your name? ")

print "Thank you" + " " + personsName + ".  Let's first create the invitation:  "

adverb1 = raw_input("Tell me a adverb: ")
partyTheme = raw_input("Tell me a theme: ")
aPlace = raw_input("Tell me a place: ")
aDayOfTheWeek = raw_input("Name a day of the week: ")
theTime = raw_input("Please tell me a time: ")
verb1 = raw_input("Tell me a verb: ")
anAnimal = raw_input("Tell me an animal: ")
bodyPart = raw_input("Name a part of your body: ")
contactInfo = raw_input("What is your email address? ")
print "\n"
print "Dear " + personsName + ","
print "You are " + adverb1 + " invited!"
print "\n"
print personsName + " is having a " + partyTheme + "party!"
print "It's going to be at " + aPlace + " on " + aDayOfTheWeek + "."
print "Please make sure to show up at " + aPlace + ", or else you will be required to " + verb1 + " a/an " + anAnimal + " with your " + bodyPart + "."
print "RSVP at " + contactInfo + "."
print "\n"
