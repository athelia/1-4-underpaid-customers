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

    #not called for in assignment, but solution shows separate first name
    first_name = customer.split()[0]

    #melons are always sold whole, thus int; but must be cast to number 
    #to do math below
    qty_melons = int(sections[2])
    #amount_paid is cast to float to support decimal differences during 
    #calculation
    amount_paid = float(sections[3])

    #how many melons from above and cost of melons (provided as an argument)
    amount_due = melon_cost * qty_melons

    #always print the actual and expected payment  
    print("{}".format(customer),
      "paid ${:.2f},".format(amount_paid),
      "expected ${:.2f}.".format(amount_due)
      )

    #how much over or under
    difference = amount_due - amount_paid 
    #check to see if the amounts match
    if amount_due != amount_paid:
      #if they don't, print a message to highlight the difference
      if amount_due > amount_paid:
        print("       {} owes ${:.2f}.".format(first_name,difference))
      else:
        print("       {} has overpaid by ${:.2f}.".format(first_name, 
          -difference))

  #close the file
  file.close()

#call the function using 1.00 as the melon cost
identify_wrong_customer_accounts(file_path = 'customer-orders.txt', 
  melon_cost = 1.00)