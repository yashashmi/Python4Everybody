# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

numList = []
largest = None
smallest = None

while True:
    userInput = input("Enter the number:")
    if userInput == "done":
        break
    num = None
    try:
        num = int(userInput)
        numList.append(num)
    except:
        print("Invalid input")
        continue

    if(largest is None):
        largest = num
    elif(largest < num):
        largest = num

    if(smallest is None):
        smallest = num
    elif(smallest > num):
        smallest = num

if(largest is not None):
    print("Maximum is", largest)

if(largest is not None):
    print("Minimum is", smallest)
