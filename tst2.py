import filecmp
import os 
path=[]
houzuifl=['.bmp','.7z','.txt'] #对不同后缀分类比较

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

for i in path:
	g = os.walk(i)
	list.extend(g)

s = []
for path,dir_list,file_list in list: 
	for file_name in file_list: 
		s.append(os.path.join(path, file_name))
		
def houzui(x,y): #从目录list：X中，挑选后缀y，返回
	s=[]
	for i in x:
		if os.path.splitext(i)[1]==y:
			s.append(i)
	return s


listhz=[]

for n in houzuifl:
	listhz.append(houzui(s,n))
		
def remove(s):		
	a=0
	js=0
	sum=(1+len(s))*len(s)/2
	for file1 in s:
		a=a+1
		s2=s[a:len(s)]
		if os.access(file1,os.F_OK):	
			for file2 in s2:
				js=js+1
				if os.access(file2,os.F_OK):		
					if filecmp.cmp(file1,file2):
						print(file1)
						print(file2)
						print(js,r"/",sum)
						print(' ')
						os.remove(file2)

def rename(s):
	a=0
	js=0
	sum=(1+len(s))*len(s)/2
	for file1 in s:
		a=a+1
		s2=s[a:len(s)]
		if os.access(file1,os.F_OK):	
			for file2 in s2:
				js=js+1
				if os.access(file2,os.F_OK):		
					if filecmp.cmp(file1,file2):
						print(file1)
						print(file2)
						print(js,r"/",sum)
						print(' ')
						os.chdir(os.path.dirname(file2))
						os.rename(os.path.basename(file2),"!!!重复的文件+++"+os.path.basename(file2))
						os.rename(os.path.basename(file1),"!!!重复的文件+++"+os.path.basename(file1))

if switch==0:
	for i in listhz:
		remove(i)
elif switch==1:
	for i in listhz:
		rename(i)
else:
	print("switch错误：switch=",switch)

