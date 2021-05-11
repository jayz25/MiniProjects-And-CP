# Problem is to split the given string into Fibonacci Sequence
'''Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.'''
def splitIntoFibonacci(S):
    for i in range(min(10,len(S))):
        x = S[:i+1] # Array Slicing Does Not consider end element.. so S[:i+1] will go till S[0] to S[i]
        # Chekcing whether it leads with 0 or not
        if x!=0 and x.startswith('0'):
            break
        a = int(x)
        for j in range(min(i+10,len(S))):
            y = S[i+1:j+1] # As mentioned above this is S[i+1] to S[j]
            # Chekcing with leading zeros
            if y!=0 and y.startswith('0'):
                break
            b = int(y)
            fib = [a,b] #This is output Fibonaaci Array consisting first two elements.. now chekcing whehter 3rd element is sum of these 2
            k = j+1
            while k < len(S):
                nxt = fib[-2] + fib[-1]
                nxtS = str(nxt)
                if nxt <= 2**31 -1 and S[k:].startswith(nxtS):
                    k+=len(S)
                fib.append(nxt)
                else:
                    break
            else:
                if len(fib)>=3:
                    return fib
    return []

