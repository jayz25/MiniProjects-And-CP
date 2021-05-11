'''T
N K D
A1 A2 A3
D= No of Days
N= No of Ppl working on problems
K= No of problems per contest
5
1 5 31
4
1 10 3
23
2 5 7
20 36
2 5 10
19 2
3 3 300
1 1 1
''' 
T = int(input())
while T!=0:
    N,K,D = map(int,input().split())
    A = []
    A = list(map(int,input().split()))
    total_problems = sum(A)
    total_contest = total_problems//K
    if total_contest>D:
        print(D)
    else:
        print(total_contest)
    T-=1


