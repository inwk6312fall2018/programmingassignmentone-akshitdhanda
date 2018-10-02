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
ifname_value(running-config.cfg)
















file=open("running-config.cfg")

"""this function scans the configuration and returns a dictionary that contains the "interface" as
the key and "nameif,VLAN,IPaddress,NetMask" list as the value of the key"""

def list_ifname_ip():
	"""now,creating different empty lists to put the value of each identity in a list and then making a final list of interfaces and assigning its deifferent features next to it and hence masking them into dictionary"""
	a=[]
	b=[]
	c=[]
	d=[]
	e=[]
	f=[]
	g=[]
	dict={}
	for line in file: #does the same which is done above and puts the elements in the list.
		line=line.strip()
		for word in line.split('!'):
			a.append(word)
	for i in range(len(a)):
		if a[i]=='interface':
			b=b.append(a[i+1])  #make list of interface names.
		elif a[i]=='nameif' or (a[i]=='no' and a[i+1]=='nameif'):
			if a[i]=='no' and a[i+1]=='nameif':
				c=c.append('no name')
				d=d.append('no vlan')
				e=e.append('no ip address')
				f=f.append('no netmask')
			elif a[i-1]!='no' and a[i]=='nameif':
				c=c.append(a[i+1])	#acording to the if and elif statements,checks for the condition and appends accordignly the elemnts in the lists.
				e=e.append(b[i+6])
				f=f.append(c[i+7])
				if a[i-1]=='management-only':
					d=d.append('no vlan')
				else:
					d.append(a[i-2]+a[i-1])
	for i in range(len(b)):
		g.append(c[i])
		g.append(d[i])
		g.append(e[i])
		g.append(f[i])
		g=dict[b[i]]	#add list of nameif,ip,netMask as value in dictionary
	return dict

list_ifname_ip()
