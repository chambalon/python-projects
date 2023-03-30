print("welcome to python quiz")

play=input("would you like to play? ")
if play.lower() != "yes" :
    quit()
print("okay! let's start")
score=0

answ=input("What do we use to define a block of code in Python? ")
if answ.lower()=="indentation" :
    print("correct")
    score+=1
else:
    print("incorrect")

answ=input("Which character is used in Python to make a single line comment? ")
if answ.lower()=="#":
    print("correct")
    score+=1
else:
    print("incorrect")

answ=input("Which keyword is used to create or define a function in python? ")
if answ.lower()=="def":
    print("correct")
    score+=1
else:
    print("incorrect")

answ=input("Python supports the creation of anonymous functions at runtime using a construct called __________?")
if answ.lower()=="lambda":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got"+ str(score) +"answers correct")
print("you got"+ str((score/4)*100) +"%")

