# __author__ = 'jathar'
# Create an implementation of the following:
#
# A line of credit product.  This is like a credit card except theres no card.
# It should work like this:
#
#   - Have a built in APR and credit limit
#   - Be able to draw ( take out money ) and make payments.
#   - Keep track of principal balance and interest on the line of credit
#   - APR Calculation based on the outstanding principal balance over real number of days.
#   - Interest is not compounded, so it is only charged on outstanding principal.
#   - Keep track of transactions such as payments and draws on the line and when
#     they occured.
#   - 30 day payment periods.  Basically what this means is that interest will not be
#     charged until the closing of a 30 day payment period.  However, when it is charged,
#     it should still be based on the principal balance over actual number of days outstanding
#     during the period, not just ending principal balance.
#
# Couple of Scenarios how it would play out:
#
# Scenario A:
#
# Someone creates a line of credit for 1000$ and 35% APR.
#
# He draws 500$ on day one so his remaining credit limit is 500$ and his balance is 500$.
# He keeps the money drawn for 30 days.  He should owe 500$ * 0.35 / 365 * 30 = 14.38$ worth
# of interest on day 30.  Total payoff amount would be 514.38$
#
# Scenario B:
#
# Someone creates a line of credit for 1000$ and 35% APR.
#
# He draws 500$ on day one so his remaining credit limit is 500$ and his balance is 500$.
# He pays back 200$ on day 15 and then draws another 100$ on day 25.  His total owed interest on
# day 30 should be 500 * 0.35 / 365 * 15 + 300 * 0.35 / 365 * 10 + 400 * 0.35 / 365 * 5  which is
# 11.99.  Total payment should be 411.99.

############----------#############

# I hope we have a discussion to review the ask in more detail, that way, we can talk through options for changing the below

# Scenario 1 is 'a'
# Scenario 2 is 'b'

from __future__ import division
from __future__ import print_function


line_of_credit=[]
def add_line_of_credit(scenario, credit_limit, apr):
    line_of_credit.append([scenario, credit_limit, apr/100])
#added lines of credit via script
add_line_of_credit('a',1000, 35)
add_line_of_credit('b',1000, 35)

transactions=[]
def transactions(scenario, day, amount):
    transactions.append([scenario,day,amount])

# added transactions w/o the function, just to show I can approach a problem multiple ways.
# The first column is the scenario
# Second column is the day the transaction happened
# Third column is the amount of transaction
transactions=[['a', 0, 500],
              ['b', 0, 500],
## used this transaction to test exceeding credit limit
#              ['b', 18, 800],
              ['b', 15, -200],
              ['b', 25, 100]
              ]

# Even though the list is already sorted,
# I wanted to make sure it's sorted by scenario and day
transactions.sort()

# Then I separated each scenario into a separate list
# The 'a' and 'b' in the if statement could be a variable
transactions_a = [x for x in transactions if x[0] == 'a' ]
transactions_b = [x for x in transactions if x[0] == 'b' ]
line_of_credit_a = [x for x in line_of_credit if x[0 ]== 'a']
line_of_credit_b = [x for x in line_of_credit if x[0] == 'b']

# This is where the monthly balance is calculated
# For each transaction scenario, I calculated the new balance and interest owed
# For payments, I made it so instead of the customer owing interest,
# the line of credit owes the customer interest.
# I summed up the total interest and outstanding balance as seperate line items.
# Lastly, I included when the customer exceeded the credit limit
interest_owed_a=0
outstanding_balance_a=0
for x in transactions_a:
    interest_owed_a = x[2]*line_of_credit_a[0][2] / 365*(30-x[1])+ interest_owed_a
    outstanding_balance_a=x[2] + outstanding_balance_a
    if outstanding_balance_a + interest_owed_a > line_of_credit_a[0][1]:
        print (x[0] , 'Exceeds line of credit at day', x[1])
        break

interest_owed_b=0
outstanding_balance_b=0
for x in transactions_b:
    interest_owed_b = x[2]*line_of_credit_b[0][2] / 365*(30-x[1])+interest_owed_b
    outstanding_balance_b=x[2]+outstanding_balance_b
    if outstanding_balance_b+interest_owed_b > line_of_credit_b[0][1]:
        print (x[0] , 'Exceeds line of credit at day', x[1])
        break

#I calculated the month end balance by adding the principal to the interest
month_end_balance_a= interest_owed_a+outstanding_balance_a
month_end_balance_b= interest_owed_b+outstanding_balance_b

print ('Scenario 1 Month End Balance $' , round(month_end_balance_a, 2), sep='')
print ('Scenario 2 Month End Balance $' , round(month_end_balance_b, 2), sep='')
