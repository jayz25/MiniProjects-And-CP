def generate_AP (a1 ,d, n):
    curr_term=a 
    for i in range(1,n+1): 
    print(curr_term, end=' ') 
    curr_term =curr_term + d




test_cases = int(input())
for i in range(test_cases):
    # Taking input from user
    a1 , d, n =int(input())
    AP_series =generate_AP(a1, d, n )
    Sqr_AP_series= list(map((lambda x :  x * x) , AP_series))
    print(Sqr_AP_Series)
    sum_sqr_AP_series =  reduce( (lambda x,y: x+y) , Sqr_AP_series)
    print(sum_sqr_AP_series)