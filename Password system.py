import time
passval2 = input("create new pass : ")
passval = input("Insert password here : ")
time.sleep(1.0)
if passval2 == passval: 
    print("Valid")
else:
    print("Not valid")