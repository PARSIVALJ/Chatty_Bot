# program to create a simple Chatty Bot
bot_name = "Touka"
birth_year = 2023

print(f"Hello! My name is {bot_name}")
print(f"I was created in {birth_year}")

user_name = input("Please,remind me your name. ")  # Recieves the user's name as input
print(f"\nWhat a great name you have, {user_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3,5 and 7 respectively")
remainder3 = int(input("Enter the value of the remainder of your age divided by 3: "))
remainder5 = int(input("Enter the value of the remainder of your age divided by 5: "))
remainder7 = int(input("Enter the value of the remainder of your age divided by 7: "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print()
print("Now I will prove to you that I can count to any number you want.")
number = int(input("Enter he number that you would like me to count up to: "))
count = 0
while count <= number:
    print(f"{count}!")
    count += 1
print("Completed, have a nice day!")
print()
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
option = int(input("Enter option: "))

while option != 2:
    print("Please,try again.")
    option = int(input("Enter option: "))

print("Congratulations, have a nice day.")


