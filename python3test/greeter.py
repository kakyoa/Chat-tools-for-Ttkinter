def get_formatted_name(frist_name,last_name):
	full_name = frist_name + ' ' + last_name
	return full_name.title()
	
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("Frist_name:")
	if f_name == 'q':
		break
		
	l_name = input("Last_name:")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")
	
 
