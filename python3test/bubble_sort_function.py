#coding=utf-8
#ð������
#�ж�һ�������Ƿ�ȫΪint��

def bubble_sort(numbs):
	for i in range(len(numbs)-1):
		for j in range(len(numbs)-i-1):
			if numbs[j] > numbs[j+1]:
				numb_t = numbs[j]
				numbs[j] = numbs[j+1]
				numbs[j+1] = numb_t
	return numbs

def strOrNumber(numbs):
	for numb in numbs:
		if numb.isdigit():
			numb_flag = True	
		else:
			numb_flag = False
			print("Enter the correct array format,'" + numb + "'")
			break
	return numb_flag
