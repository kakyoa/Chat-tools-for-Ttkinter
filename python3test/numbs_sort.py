#coding=gbk
from bubble_sort_function import*

input_numbs = input("������һ�����飺 ")

numbs = input_numbs.split(",")
 
if strOrNumber(numbs):	
	numb_lists = numbs
	for n in range(len(numbs)):
		numb_lists[n] = int(numbs[n])	
	print(bubble_sort(numbs))

		

	
