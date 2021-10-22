#Implement a simple program that generates a random password of the length supplied by
#the user.

#The password must contain at least:
#1. 1 upper case letter
#2. 1 lower case letter
#3. 1 digit
#4. 1 special character
#5. Exclude Similar Characters e.g. i, l, 1, L, o, 0, O
#6. Exclude Ambiguous Characters: { } [ ] ( ) / \ ' " ` ~ , ; : . < >
#7. The password must be at least 8 characters long.

#The program should handle any kind of error and give appropriate messages
import random
import string
max_len=8
p1=int(input("length of pwd: "))
while True:
    try:
        if("p1>=max_len"):
           print("thanks for your response")
           u=string.ascii_uppercase
           l=string.ascii_lowercase
           d=string.digits
           s=string.punctuation
           all=u+l+d+s
           temp=random.sample(all,p1)
           password=" ".join(temp)
           print(password)
           break
    except ValueError:
           print("Invalid value")
    else:
           print("please enter other value greater than 8: ")
           continue
