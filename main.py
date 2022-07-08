#If the bill was $150.00, split between 5 people, with 12% tip. 
#Welcome screen. 
print("Welcome to the tip calculator.")
#Receiving the bill amount.
amount=input("What was the total bill? $")
#Receiving the percentage of interest the customer wants to pay.
tip_percent= input("How much tip would you like to give? 10, 12, or 15? ")
#Converting recieved percentage by percent/100.
tip_percent_2= int(tip_percent)/100
#No. of people the bill is shared
people= input("How many people to split the bill? ")
#Calculating tip for each person
tip = (float(amount) * tip_percent_2) / int(people)
#/Calculating Total amount each person has to pay 
#(amount/people) + tip
each = (float(amount) / int(people)) + tip
#Round off amount
payment = round(each, 2)
#Printing results.
print(f"Each person should pay: ${payment}")
print("\n***Thanks for using spidey payment services***")
