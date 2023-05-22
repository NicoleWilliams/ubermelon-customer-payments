def check_customer_payments(filename):
    """Takes in a text file containing customer payments and check for under or overpayments.
    
    For Example: The cost of a melon is $1.00.

    Customer 3, Sally, paid 9.50 for 9 melons --> overpaid
    Customer 6, Ashley, paid 2.00 for 3 melons --> underpaid 
    """

    customer_order_data = open(filename) # open the file
    melon_cost = 1.00

    for line in customer_order_data: # loop through the lines of the file
        lines = line.split("|") # split up the lines at "|" to get a list of strings

        customer_number = lines[0] # get customer's number
        customer_name = lines[1] # get customer's full name
        melon_quantity = float(lines[2]) # get quantity of melons the customer bought
        amount_paid = float(lines[3]) # get amount the customer paid

        customer_expected = melon_quantity * melon_cost # calculate the expected price of customer's order
        if customer_expected != amount_paid: # if customer didn't pay correct amount, check if under or overpaid
            if customer_expected < amount_paid: # if customer overpaid, print overpaid
                payment_status = "overpaid"
            else:
                payment_status = "underpaid" # if customer underpaid, print underpaid

            print(f"{customer_name} has {payment_status} for their melons.")

    customer_order_data.close() # close the file
            
check_customer_payments("customer-orders.txt") # call the function
            