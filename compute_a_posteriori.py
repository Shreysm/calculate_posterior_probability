#Author:Shreyas Mohan
import sys
input=q=sys.argv[1]
ph=[{'h1':0.1,'h2':0.2,'h3':0.4,'h4':0.2,'h5':0.1}]

phc={'C|h1':1,'C|h2':0.75,'C|h3':0.5,'C|h4':0.25,'C|h5':0,
     'L|h1':0,'L|h2':0.25,'L|h3':0.5,'L|h4':0.75,'L|h5':1}

q='a'+q+'C'
x=0
out=open("result.txt","w")
out.write("Observation sequence Q: %s"%input)
out.write("\nLength of Q: %d"%len(input))

for i in range(1,6):
	x=x+phc[q[1]+'|h'+str(i)]*ph[0]['h'+str(i)]

pq=[]
pq.append({q[1]:x})


for j in range(1,len(q)-1):
	ph.append({})
	pq.append({})
	
	sum=0
	
	for i in range(1,len(ph[0])+1):
	
		ph[j]['h'+str(i)]=phc[q[j]+'|h'+str(i)]*ph[j-1]['h'+str(i)]/pq[j-1][q[j]]

		sum+=phc[q[j+1]+'|h'+str(i)]*ph[j]['h'+str(i)]
	pq[j][q[j+1]]=sum
	out.write("\n\nAfter Observation %d= %s\n"%(j,q[j]))
	for i in range(1,len(ph[0])+1):

		out.write("\nP(h%d|Q)= %.5f"%(i,ph[-1]["h"+str(i)]))
	if q[j+1]=="C":
		out.write("\n\nProbability that the next candy we pick will be C, given Q: %.5f"%pq[-1]["C"])
		out.write("\nProbability that the next candy we pick will be L, given Q: %.5f"%(1-pq[-1]["C"]))
	elif q[j+1]=="L":
		out.write("\nProbability that the next candy we pick will be C, given Q: %.5f"%(1-pq[-1]["L"]))
		out.write("\nProbability that the next candy we pick will be L, given Q: %.5f"%(pq[-1]["L"]))

out.close()
