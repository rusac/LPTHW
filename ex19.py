def cheese_and_crackers(cheese_count, boxes_of_crackers):           # 'def' defines the function
    print "You have %d cheeses!" % cheese_count                     # Lines 2-5 are part of this function
    print "You have %d boxes of crackers!!" % boxes_of_crackers     # 'cheese_and_crackers'.
    print "Man that's enough for a party!"
    print "Get a blanket.\n"                                        # Line break for readability bc we call the
                                                                    # function multiple times below.

print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)                                         # Simply typing the fxn here will call it.
                                                                    # Note how TWO values are used, as our definition
                                                                    # for the function uses TWO values **see line 1**
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)           # Our function, instead of using 'cheese_count'
                                                                    # and 'boxes_of_crackers' is instead using two
                                                                    # different variables - 'amount_of_cheese' and
print "We can even do math inside too:"                             # 'amount_of_crackers', both of which have been
cheese_and_crackers(10 + 20, 5 + 6)                                 # defined in Lines 13 and 14.


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  # Our fxn can use variables and values and 
                                                                        # combinations of both.

cheese_and_crackers(2, 5)
