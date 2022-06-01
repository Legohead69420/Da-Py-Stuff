import time
print("Welcome to the most advanced AI in the world")
print("AI : What's Your Name")
name = input("You : ")#Creates an int  for the user's "name"
print(" ")
print("AI : Where Are You From")
country = input("You : ")#Creates an int for the user's "country"
print(" ")
print("AI : What's Your Hobby")
hobby = input("You : ")#Creates an int for the user's "hobby"
print(" ")
print("AI : What's Your Gender")
gender = input("You : ")#Creates an int for the user's gender 
print(" ")
print("AI : When Were You Born")
#Calculation for user age
val1 = float(input("Year : "))
val2 = float(input("Month(requires month number or AI will fail to work) : "))
curyear = 2022
val3 = (curyear * 12) + 3
val4 = (val1 * 12) + val2
age = (val3 - val4) / 12
#End of calculation
print("Processing...")
time.sleep(3.0)
print("AI : ")
print("There Name Is : ",(name))
time.sleep(1.0)
print("Was Born In : ",(country))
time.sleep(1.0)
print("Who Enjoys : ",(hobby))
time.sleep(1.0)
print("Is : ",(gender))
time.sleep(1.0)
print("Is : ",(age))
time.sleep(1.0)
print("Was this correct")
correct = input("Yes Or No : ")
if correct == ("Yes"):
    print("Thank you for your support")
elif correct == ("No"):
    print("Thank you for your support")
    