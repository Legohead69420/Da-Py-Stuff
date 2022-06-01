import random
import time
errortrue = random.randint(1, 319)
errorcode = random.randint(39, 3999)
if errortrue == (1):
    print("An Error Has Occured Please Restart The Program. Error Code :",(errorcode))
    print("<restart>")
else:
    number = "0123456789" #numbers
Use_for = number #Use_for is just combining all characters
length_for_pass = 2 #password length
num = "".join(random.sample(Use_for, length_for_pass)) #creating the number part of the hash from the Use_for integer
import random
lower_case = "abcdefghijklmnopqrstuvwxyz" #lower case letters
Use_for = lower_case #Use_for is just combining all characters
length_for_pass = 6 #password length
letter = "".join(random.sample(Use_for, length_for_pass)) #creating the letter part of the hash from the Use_for integer
out = num + letter
print("Generating Hash...")
time.sleep(0.3)
print("Hash :",(out))
