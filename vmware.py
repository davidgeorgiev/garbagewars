try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import urllib
import random

SERVER_HOST="http://192.168.204.131:8080"

OBJECTS_API = "/api/sector/%d/objects"
ROOTS_API = "/api/sector/%d/roots" 
COMPANY_API = "/api/sector/%d/company/mdk/trajectory"
system = []


def get_objects(sector):
	url=SERVER_HOST+OBJECTS_API%sector
	#print (url)
	res=urllib2.urlopen(url)
	edges = []
	for line in res.readlines():
		line=line.strip().split(' ')
		nodes=[int(s) for s in line]
		# #print (nodes)
		edges.append(nodes)
	return edges
	
def get_roots(sector):
	url=SERVER_HOST+ROOTS_API%sector
	#print (url)
	res=urllib2.urlopen(url)
	nodes = []
	for line in res.readlines():
		node=int(line.strip())
		nodes.append(node)
	return nodes

def post_method(line,sector):
	'''url=SERVER_HOST+COMPANY_API%sector#trajectory
	values = line
	#print ("---------------------------values:")
	#print (values)
	#print ("---------------------------")
	data = urllib.urlencode(values)
	#print ("---------------------------data:")
	#print (data)
	#print ("---------------------------")
	req = urllib2.Request(url, data)
	#print ("---------------------------req:")
	#print (req)
	#print ("---------------------------")
	response = urllib2.urlopen(req)
	#print ("---------------------------response:")
	#print (response)
	#print ("---------------------------")
	the_page = response.read()
	#print ("---------------------------the_page:")
	#print (the_page)
	#print ("---------------------------")
	'''
	urllib2.urlopen(SERVER_HOST+COMPANY_API%sector, line)
	edges = get_objects(current_sector)	
	nodes = get_roots(current_sector)


current_sector = 1
edges = get_objects(current_sector)	
nodes = get_roots(current_sector)
#print (edges[0])

system=nodes

#print(system)
#print(nodes)

def istnext(edge,edges): #edge[j]
	k = 0
	#print("NODE:")
	#print(edge)
	while(len(edges)>k):
		if(edge==edges[k][0]):
			#print(edges[k])
			if not(edges[k][0] in system):
				system.append(edges[k][0])
			if not(edges[k][1] in system):
				system.append(edges[k][1])
			#print(edges[k][1])
			#print("................")
		k+=1

def get_trajectory(system,edges):
	i = 0
	again = 1
	temp = []
	end_loop = 0
	rand = random.randint(0,len(edges)-1)
	while(again):
		if not(edges[rand][0] in system):
			my_edge = edges[rand][0]
			again = 0
		else:
			return 13
	if not(my_edge in temp):
		temp.append(my_edge)
		#print (my_edge)
	while((len(edges)>i) and (end_loop == 0)):
		if(my_edge==edges[i][1]):
			if not(edges[i][0] in temp):
				my_edge = edges[i][0]
			first_time_here = 0
			i = 0
			if not(my_edge in temp):
				temp.append(my_edge)
				#print (my_edge)
			else:
				end_loop = 1
		i+=1
	print("Start creating trajectory...")
	i = 0
	end_loop = 0
	del temp[:]
	start_edge = my_edge
	if not(my_edge in temp):
		temp.append(my_edge)
		#print (my_edge)
	while((len(edges)>i) and (end_loop == 0)):
		
		if(my_edge==edges[i][0]):
			my_edge = edges[i][1]
			i = 0
			if ((not my_edge in temp) and (not my_edge in system)):
				temp.append(my_edge)
				#print (my_edge)
			else:
				end_loop = 1
		i+=1
	return temp
i = 0
while(len(system)>i):
	istnext(system[i],edges)
	i+=1
#print(system)
i = 0
#trajectory = []
#while(8 > i):
#	trajectory[i].append(get_trajectory(system,edges))
#	i+=1
while(1):
	#print("sector")
	#print(current_sector)
	
	trajectory = get_trajectory(system,edges)
	print(trajectory)
	if (trajectory == 13):
		current_sector = random.randint(1,10)
		edges = get_objects(current_sector)	
		nodes = get_roots(current_sector)
		system = nodes
		counter = 0
		while(len(system)>counter):
			istnext(system[counter],edges)
			counter+=1
		#print(system)
	else:
		trajectory = map(str, trajectory)
		trajectory = "trajectory="+' '.join(trajectory)
		#print(trajectory)
		post_method(trajectory,current_sector)














#print("=============EDGES=============")
#print(edges)
#print("===============================")



#print(edges)
#print(nodes)


'''
def el(ed, nd):
	#print(nd)
	i = 0
	j = 0
	while(len(nd) > i):
		j = 0
		#print("NODE:--------------------")
		#print(nd[i])
		while(len(ed) > j):
			if(nd[i] == ed[j][0]):
				if not(ed[j][0] in system):
					system.append(ed[j][0])
					istnext(ed[j][1],ed)
				#print(ed[j])
				
				
			j+=1
		i+=1

	#print(system)

el(edges, nodes)
#print(edges)


#------------------------------------------------------------------------
post_method(edges[0],1)
#print edges


#print "------------------------------------------------------------"
i = 0
while(i < len(edges)):
	#print edges[i]
	edges[i]
	i+=1


edges = get_objects(3)		
#print edges

edges = get_objects(4)		
#print edges

roots = get_roots(2)
#print roots

roots = get_roots(3)
#print roots

pm = post_method(edges,roots,2)
#print pm
'''
