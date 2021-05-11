subsuq_list=[];
consec=[];
n = int(input());
for i in range(n):
	k=int(input());
	subsuq_list.append(k)
print(subsuq_list)	
i = 0
for a in subsuq_list:	
	if a%(2**i)==1:
		consec.append(subsuq_list[a])	
	i+=1
print(consec)