"""function to create a list of "access-list" for "global_access" and "fw-management_access_in"""
def list_access():
	file=open("running-config.cfg") #opens the mentioned file from directory
	my_lst=[] #creates an empty list
	for line in file:
		line=line.strip()
		for i in line.split():    #creates a list of words
			if i=='global_access' or i=='fw-management_access_in':	#checks for condition
				my_lst.append(line) #appends line if satisfying condition.
	print(my_lst)
	
list_access()
