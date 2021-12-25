#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")


bill_total = float(input("What was the total bill? $"))
tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? " ))
diners = int(input("How many people to split the bill? "))
total_tip = (tip_amount/100)*bill_total
#Force the formating EX / 150 , 12 , 5
total_per_person = "{:.2f}".format(round(((bill_total+total_tip)/diners),2))

print(f"Each person should pay: ${total_per_person}")
