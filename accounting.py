def identify_wrong_customer_accounts(file_path, melon_cost):
  """Parse a file & melon cost to identify customers who have under or overpaid.

  Takes in a string file_path and a float melon_cost and prints to the console 
  when the expected payment for a customer does not match actual payment.

  """
  
# open the file at the path passed in as an argument
  file = open(file_path)

  #iterate through every line and format:
  for line in file:
    #remove trailing whitespace e.g. newline (superfluous this time)
    line = line.rstrip()

    #split the line into pieces at the divider character
    sections = line.split('|')
    
    #assign the various sections to more identifiable variables
    customer = sections[1]

    #melons are always sold whole, thus int; but must be cast to number 
    #to do math below
    qty_melons = int(sections[2])
    #amount_paid is cast to float to support decimal differences during 
    #calculation
    amount_paid = float(sections[3])

    #how many melons from above and cost of melons (provided as an argument)
    amount_due = melon_cost * qty_melons

    #check to see if the amounts match
    if amount_due != paid:
      #if they don't, print a message to highlight the difference
      print("{}".format(customer),
        "paid ${:.2f},".format(amount_paid),
        "expected ${:.2f}.".format(amount_due)
        )

  #close the file
  file.close()

#call the function using 1.00 as the melon cost
identify_wrong_customer_accounts(file_path = 'customer-orders.txt', 
  melon_cost = 1.00)

"""
#set the melon cost
melon_cost = 1.00

#define some variables for customer 1 - customer name, 
#quantity of melons, and what they have paid
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

#repeat for customer 2 all the way through customer 6
customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

# expected cost is the product of the number of melons and the cost
customer1_expected = customer1_melons * melon_cost
# if the expected isn't the same as the paid cost, print...
if customer1_expected != customer1_paid:
  # the paid and expected costs in human readable format. 
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

#repeat the same process for all the customers....
customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
"""