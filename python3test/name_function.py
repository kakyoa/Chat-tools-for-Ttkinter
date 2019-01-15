
def get_formatted_name(frist,last,middle=""):
	if middle:
		full_name = frist + " " + middle + " " + last
	else:
		full_name = frist + " " + last
	return full_name.title()
		


