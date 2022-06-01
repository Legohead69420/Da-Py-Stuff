import random
lower_case = "abcdefghijklmnopqrstuvwxyz" #lower case letters
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #upper case letters
number = "0123456789" #numbers
symbols= "@#$%&*/\?" #symbols
Use_for = lower_case + upper_case + number + symbols #Use_for is just combining all characters
length_for_pass = 10 #password length
password = "".join(random.sample(Use_for, length_for_pass)) #creating a password from the Use_for integer
print("Your random password is :") #print user friendly text into the powershell terminal
print(password) #print password into the terminal