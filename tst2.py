import filecmp
import os 
path=[r"D:\test1",r"D:\test2"]
list=[]
finallist=[]
xt=[]
for i in path:
	g = os.walk(i) 
	list.extend(g)

s = []
for path,dir_list,file_list in list: 
	for file_name in file_list: 
		s.append(os.path.join(path, file_name))
		
a=0
js=0
sum=(1+len(s))*len(s)/2
for file1 in s:
	a=a+1
	s2=s[a:len(s)]
	for file2 in s2:
		js=js+1
		
		if filecmp.cmp(file1,file2):
			print(file1)
			print(file2)
			print(js,r"/",sum)
			print(' ')
			xt.append(file1)
			xt.append(file2)
			finallist.append(xt)
			xt=[]

def hebing1(x):	
	finallist0=x
	finallist1=x
	b=0			
	for n in finallist1:
		b=b+1
		finallist2=finallist1[b:len(finallist1)]
		for m in n:
			c=0
			for p in finallist2:
				c=c+1
				for q in p:
					if m == q:
						finallist0[b-1]=p+n
						finallist0.pop(b+c-1)
						return finallist0
	return "final"



while True:
	a1=hebing1(finallist)
	if "final"!=a1:
		finallist=a1
	else:
		break

def shanchu(x):
	finallist1=x
	finallist0=x
	b=0		
	for i in finallist1:
		b=b+1
		c=0
		for n in i:
			c=c+1
			for m in i[c:len(i)]:
				if n == m:
					finallist0[b-1].pop(c-1)
					return finallist0
	return "final"

while True:
	a2=shanchu(finallist)
	if a2!="final":
		finallist=a2
	else:
		break
	

print(finallist)

z=0
for i2 in finallist:
	z=z+1
	finallist[z-1].pop(0)
print(finallist)

for i3 in finallist:
	for i4 in i3:
		os.remove(i4) 
			
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
			
			
