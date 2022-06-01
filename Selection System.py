import time
import random
selection = input("Input Selection Here : ")
errorcode = random.randint(31, 3183)
if selection == ("1"):
    print("Selected : 1")
    time.sleep(1.0)
    print("Restart Program To Select New Option")
elif selection == ("2"):
    print("Selected : 2")
    time.sleep(1.0)
    print("Restart Program To Select New Option")
elif selection == ("3"):
    print("Selected : 3")
    time.sleep(1.0)
    print("Restart Program To Select New Option")
else:
    print("An Error Has Occured Please Restart The Program. Error Code :",(errorcode))