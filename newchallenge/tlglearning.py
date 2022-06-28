#!/usr/bin/env python3

import random

wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

num= input("choose a number between 0 and 18: ")

if num.isdigit():
    num= int(num)
    student_name= tlgstudents[num]

elif num == "random":
    student_name= random.choice(tlgstudents)

else:
    student_name= num

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
