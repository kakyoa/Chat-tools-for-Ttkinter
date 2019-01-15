#coding=gbk
from bubble_sort_function import *

a = open("numbs.txt")
txt_numbs = a.readline()
#print(txt_numbs)
numbs = txt_numbs.split(",")

if strOrNumber(numbs):
	numb_lists = numbs
	for n in range(len(numbs)):
		numb_lists[n] = int(numbs[n])	
	print(bubble_sort(numb_lists))
a.close()	

