"""This function is so designed that it has empty lists at first from i1 to i4 and then the file is converted into a list of separated wordsin i1 and then it looks up for if there is no ip address mentioned,puts them into list 2 which is i2 and if the element has 172 or 192 as first element of ip address,it deletes the first element and hence it inserts 10 at that point which is put into list i4,which is our required list."""


def ip_address():
	my_file=open("running-config.cfg")
	i1=[]
	i2=[]
	i3=[]
	i4=[]
	i5=[]
	for line in my_file:
		line=line.strip()
		for word in line.split():
			i1.append(word)
	for i in range(len(i1)):
		if i1[i-1]!='no' and (i1[i]=='ip' and i1[i+1]=='address'):
			i2.append(i1[i+2])
	for i in i2:
		i3.append(i.split('.'))
	for i in i3:
		del i[0]
		i.insert(0,'10')
		i4.append('.'.join(i))
	return i4

	for i in range(len(i1)):
                if i1[i-1]!='no' and (i1[i]=='Security-level':
                        i5.append(i1[i+2])
	for i in i5:
		del i[0]
                i.insert(0,'10')
	return i5

print(ip_address)
