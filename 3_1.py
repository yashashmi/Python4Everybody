#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly. 

hours = input("Enter the hours")
fhours = float(hours)
rate = input("Enter the rate")
frate = float(rate)
if fhours <= 40.0:
    pay = fhours * frate
else:
    extraHours = fhours - 40
    pay = extraHours * (1.5 * frate)
    pay = pay + (40 * frate) 
print(pay)