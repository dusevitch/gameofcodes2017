import time
st = time.time()
a="-+--++--"
s=0
l=[]
for idx,i in enumerate(a):
	sP=s
  	if i=="+":
  		s+=1
  	else:
  		s=-1
  	if sP>=0 and s<0:
  		l.append(idx+1)
print l
print time.time()-st