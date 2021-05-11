'''Your program has currencies of Rs. 1, 5, 10, 20, 100, 500, 2000.
Your user enters a bill amount say Rs. 243.
Your user then enters a cash given say Rs. 2000.
Now, help the user by telling how can he/she return the change to the customer with minimum number of notes? '''
bill_amount = int(input())
cash_give = int(input())
no_of_notes = 0
notes = [2000,500,100,20,10,5,1]
k = cash_give - bill_amount 
for i in notes:
    no_of_notes = no_of_notes + (k//i)
   # print(no_of_notes)
    k = k%i
   # print(k)
    
print(no_of_notes)