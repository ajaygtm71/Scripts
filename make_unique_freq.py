def minRemoval(str):
	frequencies = dict()
	for c in str:
		if c not in frequencies:
			frequencies[c]=str.count(c)	
	pq=list()
	for x in frequencies.values():
		pq.append(x)
	pq= sorted(pq,reverse=True)
	count=0
	while(len(pq)>1):
		top  = pq.pop(0)
		if top==pq[0]:
			if top>1:
				pq.append(top-1)
				pq= sorted(pq,reverse=True)
			count+=1
	return count

if __name__=="__main__":
	str= "abbbcccd"
	print("minimum removals for unique frequencies are: ", minRemoval(str))
