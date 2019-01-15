#coding=gbk

input_numbs = input("请输入一个数组： ")
numbs = input_numbs.split(",")
numb_flag = True 
for numb in numbs:
	if numb.isdigit():
		print(numb)
	else:
		numb_flag = False
		print("请输入正确的数组格式0.0")
		break
#print(numb_flag)
print(numbs)

if numb_flag:		
	for i in range(len(numbs)-1):
		for j in range(len(numbs)-i-1):
			if numbs[j] > numbs[j+1]:
				numb_t = numbs[j]
				numbs[j] = numbs[j+1]
				numbs[j+1] = numb_t
	print(numbs)
		

	
