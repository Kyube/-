import filecmp
import os 
path=[]

while True:
	switch=int(input('0.删除重复文件\n1.重命名重复文件\n请输入：')) # switch=0 删除重复文件，switch=1 重命名重复文件
	
	if switch==0:
		print("\nswitch等于0,删除重复文件")
		break
	elif switch==1:
		print("\nswitch等于1,重命名重复文件")
		break
	else:
		print("\n错误，switch超出允许值，switch=",switch,'请重新输入\n')

def cclist(x,y): #x:list 检查y在表X中是否存在
	for i in x[0:len(x)-1]:
		if i==y:
			return 'XT'
	return 'BT'
		
while True:
	path.append(input('\n输入要查重的目录：'))
	if cclist(path,path[len(path)-1])=='XT':
		path.pop(len(path)-1)
		print('已输入过相同目录')
	if path[len(path)-1]=='f':
		path.pop(len(path)-1)
		break
	print('\n可继续输入目录，输入f结束')

print('\n选择的switch是：')
if switch==0:
	print("switch等于0,删除重复文件")
elif switch==1:
	print("switch等于1,重命名重复文件")
else:
	print('错误，switch超出允许值')
	
def dayinglist(x):#打印list
	for i in x:
		print(i)
		
print('\n要检查的目录是：')
dayinglist(path)

while True:
	if input('\n请确认上述信息，继续，请输入y:')=='y':
		break


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

if switch==0:
	z=0
	for i2 in finallist:
		z=z+1
		finallist[z-1].pop(0)
	print(finallist)

	for i3 in finallist:
		for i4 in i3:
			os.remove(i4) 		
elif switch==1:
	for i5 in finallist:
		for i6 in i5:
			os.chdir(os.path.dirname(i6))
			os.rename(os.path.basename(i6),"!重复的文件+"+os.path.basename(i6))
else:
	print("switch错误：switch=",switch)
