"""JTC_2022 Project #1: Tip Calculator written in Python


This is the first project for the JTC_2022 Spring cohort at the Columbia School of Business Justice thru Code software engineering development
program. The Tip Calculator inputs a customer's data, the price of the meal or other service, and calulates the tip, sales tax, and the final bill for
the customer; or the customer can enter a fixed amount, fixed_tip_amount, as the tip.

The project was written in the Python programming language in March 2022.

# Design specification:

**Input data:**

  food_costs = float
  
  number_splitting_bill = int
  
  sales_tax = float
  
  the_bill = float
  
  tip_amount = float
  
  fixed_tip_amount = float
  
  tip_perc = float
  
 # **Decisional logic:**
 
 The decisional logic is just adding and multiplication of variables.
 
 The data structures are int and floats
 
 A variable is created to sum the input data: total_bill multiplied by the tip_amount:  total_bill = the_bill * tip_amount : float
 """

 
food_cost = float(input("Please input the total costs of the food?   "))

people_in_party = int(input("How many people are splitting the bill?   "))


tip_perc = float(input("""What percentage of the bill would you like to tip: It is customary for excellent service to tip 20% (.20); for great service 15% (.15); and for good service 12.5% (.125). Please input .2 for 20% or .15 for 15% or .125 for 12.5% or you can enter a fixed tip amount in dollars.
 """  ))

sales_tax = .10

the_bill = food_cost + food_cost*sales_tax

print("The bill is $", the_bill)

tip_amount = the_bill * (tip_perc)

total_bill = the_bill + tip_amount 
print()

print("The bill plus taxes is $", total_bill)

#print(f"The Total bill plus taxes is {$ total_bill}")

print("The tip amount is $ ", tip_amount)

costs_per_person = total_bill / people_in_party

print("The costs per person is $" , costs_per_person)
print()
print()


print("Thank you for dining with us.")