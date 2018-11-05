import filecmp
import os 

path=[r'D:\test1',r'D:\test2']
list=[]
for i in path:
	g = os.walk(i)
	list.extend(g)

s = []
for path,dir_list,file_list in list: 
	for file_name in file_list: 
		s.append(os.path.join(path, file_name))

# list_i=[]
list_path=set()		
for i in s:
	if i.find('!!!重复的文件+++')!=-1:
		list_path.add(i)
		
for i in list_path:
	s.remove(i)

for i in list_path:	
	print(i)
print(' ')

for i in list_path:	
	print(s)
print(' ')

js=0
sum=len(s)*len(list_path)
for m in list_path:
	for n in s:
		js=js+1
		if os.access(n,os.F_OK):
			if filecmp.cmp(m,n):
				print(m)
				print(n)
				print(js,r"/",sum)
				print(' ')
				os.chdir(os.path.dirname(n))
				os.rename(os.path.basename(n),"!!!重复的文件+++"+os.path.basename(n))
		
