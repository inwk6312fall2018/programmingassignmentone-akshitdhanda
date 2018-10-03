file=open("running-config.cfg")         #this opens the file which is directed to here.
"""The following function Returns a list that contains the tuple of interfacename and value of nameif"""
def ifname_value():
	"""Now, making list of different set of information in the intial list and hence creating empty lists for the same for combining different entries in the last list"""	

	a=[]
	b=[]
	c=[]
	d=[]
	for line in file:
		line=line.strip() #strip off the whitespaces
		for word in line.split('!'): #splits the whole information on basis of !.
			a=a.append(word)
	for i in range(len(a)):
		if a[i]=="interface":
			b=b.append(lst1[i+1]) #making a list of the interface names
		elif a[i]=='nameif' or (a[i]=='no' and a[i+1]=='nameif'):
			if a[i]=='no' and a[i+1]=='nameif': #searchs for no name if and appends no name to next list
				c=c.append("no name")
			elif a[i-1]!="no" and a[i]=="nameif":
				c=c.append(a[i+1])#if it is not that,it appends the next word to c.
	for i,j in zip(b,c):		#Zips elements of 2 lists to make list of tuple (interface,interface name)
		d.append((b[i],c[i]))
	return d
ifname_value()
