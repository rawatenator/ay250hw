import numpy as N
import matplotlib.pylab as plt
from matplotlib.mlab import csv2rec
import os
import sqlite3
from cStringIO import StringIO
import webbrowser



path = os.path.abspath(os.path.dirname(__file__))






#the polls data and the names data that were given both list states. However, the rankings only list the 
#long version: CALIFORNIA, whereas the name data only list the abbreviation. I downloaded a list of
#full names and abbreviations and read the data into a table to simplify later joins.
def q0():
	'''#the polls data and the names data that were given both list states. However, the rankings only list the 
	#long version: CALIFORNIA, whereas the name data only list the abbreviation. I downloaded a list of
	#full names and abbreviations and read the data into a table to simplify later joins.'''
	# MAKE A TABLE TO CONVERT BETWEEN 2 LETTER ABBREVIATIONS AND FULL STATE DESCRIPTIONS
	staterecarray = csv2rec(path+"/state2letters.txt",delimiter='\t')
	
	sql_cmd = '''CREATE TABLE  statetable(fullname TEXT, abrev text)'''
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	cursor.execute(sql_cmd)
	
	for state in staterecarray:
		sql_cmd = "INSERT INTO statetable(fullname, abrev) VAlUES ('%s','%s')" % (state['state'].upper(),state['abrev'])
		cursor.execute(sql_cmd)
	connection.commit()
	connection.close()
	
	
def getabrevfromfull(statenamefull):
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	cmd = 'SELECT statetable.abrev FROM statetable Where statetable.fullname = "%s" ' % statenamefull
	cursor.execute(cmd)
	dbinfo = cursor.fetchone()
	for entry in dbinfo: abreviation = entry
	return abreviation
	
	
	
	

#answer to question 1: import senate polling data to sqlite3
def q1(filename=path+"/senate_polls.csv"):
	'''#answer to question 1: import senate polling data to sqlite3'''
	#make rec array from the polling data
	senate_recarray = csv2rec(filename)

	#make a database/connect, poll_db
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()

	#make table, 'rankings'
	sql_cmd = '''CREATE TABLE  rankings (id INTEGER PRIMARY KEY AUTOINCREMENT, day INTEGER,len INTEGER, state TEXT, dem INTEGER,\
	rep INTEGER, indep INTEGER, month int,dayofmonth int, poll text)'''
	cursor.execute(sql_cmd)

	#read data into 'rankings;
	for datapoint in senate_recarray:
		sql_cmd = 'INSERT INTO rankings (day, len, dem, rep, indep, month, dayofmonth, state,poll) \
		VALUES (%i,%i,%i,%i,%i,%i,%i,"%s","%s")' % (int(datapoint['day']), 
		int(datapoint['len']), 
		datapoint['dem'],
		datapoint['gop'],
		datapoint['ind'], 
		datapoint['date'].month,
		datapoint['date'].day,
		datapoint['state'].upper(),
		datapoint['pollster'])
	
		cursor.execute(sql_cmd)
	#finalize data
	connection.commit()

	#print data to check entry
	sql_cmd = "SELECT * from rankings where day > 1"
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchall()
	for entry in dbinfo: print entry





#question 2:SIMILAR TO Q1, EXCEPT FROM candidate_names.txt
def q2():
	'''#question 2:SIMILAR TO Q1, EXCEPT FROM candidate_names.txt'''

	#read data into recarray
	candidate_names_recarray = csv2rec(path+"/candidate_names.txt")
	#connect to database:
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	#make table called: candidate names
	sql_cmd = "CREATE TABLE  candidate_names(state TEXT, democrat text, republican text, independent text, incumbentparty text )"
	cursor.execute(sql_cmd)
	#read info into table
	for each in candidate_names_recarray:
		sql_cmd = '''INSERT INTO candidate_names(state,democrat,republican,independent,incumbentparty) VALUES\
		("%s","%s","%s","%s","%s")''' % (each["state"].strip(),each["democrat"].strip(),each["republican"].strip(),each["independent"].strip(),each["incumbentparty"].strip())
		cursor.execute(sql_cmd)
	connection.commit()
	#print data to confirm:
	sql_cmd = "SELECT * from candidate_names"
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchall()
	for entry in dbinfo: print entry



#question 3: I downloaded the pictures of the candidates.
# here, I get the paths to the images and the names of the candidate
# and store these data in a table
def q3():
	'''#question 3: I downloaded the pictures of the candidates.
	# here, I get the paths to the images and the names of the candidate
	# and store these data in a table'''
	name = []
	picture_path = []
	listdir = os.listdir(path+'/candidates')
	for each in listdir:
		name.append( each.split('.')[0] )
		picture_path.append('candidates/'+ str(each))

	#connect,make table
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	sql_cmd = "CREATE TABLE  images(name TEXT,url TEXT)";
	cursor.execute(sql_cmd)

	#insert data
	for each in xrange(len(name)):
		sql_cmd = 'INSERT INTO images(name,url) VALUES ("%s","%s")' % (name[each],picture_path[each])
		cursor.execute(sql_cmd)
	connection.commit()

	#test entry
	sql_cmd = "SELECT * from images"
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchall()
	for entry in dbinfo: print entry

	connection.close()
	










# q4: HERE I PERFORM the necessary joins so the three tables are in sync.
#to simplify readability, here are the tables and thier columns:
#candidate_names(state TEXT, democrat text, republican text, independent text, incumbentparty text );
#images(name TEXT,url TEXT);
#rankings (id INTEGER PRIMARY KEY AUTOINCREMENT, day INTEGER,len INTEGER, state TEXT, dem INTEGER,rep INTEGER, indep INTEGER, month int,dayofmonth int, poll text);
#this function eventually makes a webpage and displays the candidates newest poll data, and thier photographs, as well as other data
def q4():
	'''# q4: HERE I PERFORM the necessary joins so the three tables are in sync.
	#to simplify readability, here are the tables and thier columns:
	#candidate_names(state TEXT, democrat text, republican text, independent text, incumbentparty text );
	#images(name TEXT,url TEXT);
	#rankings (id INTEGER PRIMARY KEY AUTOINCREMENT, day INTEGER,len INTEGER, state TEXT, dem INTEGER,rep INTEGER, indep INTEGER, month int,dayofmonth int, poll text);
	#this function eventually makes a webpage and displays the candidates newest poll data, and thier photographs, as well as other data'''
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	
	#get stateinput from user
	state = raw_input('enter the 2digit abbreviation for a state: ').upper()

	#get variable: incumbent
	sql_cmd = "SELECT candidate_names.incumbentparty from candidate_names where candidate_names.state = '%s' " % state
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchone()
	incumbent = ''
	for entry in dbinfo: incumbent = entry.upper()

	
	#NOTE, because the original data were ordered by date, there is no need to sort through the data and choose the most row. Generally this can be accomplished
	#by "select * from nssdlkj ORDER BY..."; I will only fetch the first result from the query



	#get republican rankings: After joining images, candidate_names, rankings, this query returns the name of the candidate, his ranking, the month, day, and url of his photograph
	#Becasue rankings.state uses full names for states, there is a join with the table "statetable"
	sql_cmd = '''SELECT candidate_names.republican, rankings.rep, rankings.month, rankings.dayofmonth, images.url from rankings Left Join statetable on rankings.state = statetable.fullname\
	 left join candidate_names on candidate_names.state = statetable.abrev left join images on images.name = candidate_names.republican
	Where "%s" = candidate_names.state  '''% state
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchone()
	rep = []
	for entry in dbinfo: rep.append(entry)
	
	
	
	
	#similar 
	sql_cmd = '''SELECT candidate_names.democrat, rankings.dem, rankings.month, rankings.dayofmonth, images.url from rankings Left Join statetable on rankings.state = statetable.fullname\
	 left join candidate_names on candidate_names.state = statetable.abrev left join images on images.name = candidate_names.democrat
	Where "%s" = candidate_names.state  '''% state
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchone()
	dem = []
	for entry in dbinfo: dem.append(entry)
	
	#similar to above
	sql_cmd = '''SELECT candidate_names.independent, rankings.indep, rankings.month, rankings.dayofmonth, images.url from rankings Left Join statetable on rankings.state = statetable.fullname\
	 left join candidate_names on candidate_names.state = statetable.abrev left join images on images.name = candidate_names.independent
	Where "%s" = candidate_names.state  '''% state
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchone()
	ind = []
	for entry in dbinfo: ind.append(  entry)
	
	connection.close()

	#This function tests to see if the incumbent party is in the lead
	def party_change():
		d = {'REPUBLICAN':rep[1],'DEMOCRAT':dem[1],'INDEPENDENT': ind[1]}#dem[1],rep[1],ind[1] refers to the number of points that the candidate currently has in the polls
		maxinpolls = max(d,key = lambda x: d[x]) #determines which party has the highest number of points by sorting through the dictionary
		if incumbent == maxinpolls:
			return "The %s incumbent will likely keep his/her seat"%(incumbent)
		else:
			return "The %s incumbent will likely lose his/her seat to the %s party candidate"%(incumbent, maxinpolls )
	
	
	incumbent_statement = party_change()
	
	
	
	#make the web page
	def generate_web_page():
		if ind[1] == (-1): #test to see if independent candiate is existent;
			indstatement = ''
		else:
			indstatement = '	<tr> <td> INDEPENDENT </td> <td> %s </td> <td> %s </td>  <td> <img src="%s"></img> </td> </tr>'%(ind[0],ind[1],ind[4])
		
		output = open(path + '/webinfo.html',"w")
		output.write('''
		<h1 name='state'>%s</h1>
		<h2 name='incumbentstatus'>%s</h2>
		<table>
		<tr> <td> party </td> <td> name </td> <td> current poll numbers </td>  <td> picture </td> </tr>
		<tr> <td> DEMOCRAT </td> <td> %s </td> <td> %s </td>  <td> <img src="%s"></img> </td> </tr>
		<tr> <td> REPUBLICAN </td> <td> %s </td> <td> %s </td>  <td> <img src="%s"></img> </td> </tr>
		%s
		
		
		poll taken on %i-%i-2010
		</table>'''% (state, incumbent_statement, dem[0],dem[1],dem[4], rep[0],rep[1],rep[4],indstatement, dem[2],dem[3]))
		output.close()
		webbrowser.open_new(path+ '/webinfo.html')
		
	generate_web_page()









#Q5 : HOW MANY DEMOCRATS WILL LOSE IN THE ELECTION CYCLE?
# this function answers the question, how many elections will the dems lose. It goes state by state, doing a query per state. If the dem's most recent 
#poll score is less than the rep's or the ind's, then the democrat is said to have lost that state, democrat losses +=1

def q5():
	'''#Q5 : HOW MANY DEMOCRATS WILL LOSE IN THE ELECTION CYCLE?
	# this function answers the question, how many elections will the dems lose. It goes state by state, doing a query per state. If the dem's most recent 
	#poll score is less than the rep's or the ind's, then the democrat is said to have lost that state, democrat losses +=1
	'''
	#connect
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()

	#make a list of the states
	sql_cmd = " SELECT statetable.abrev from statetable"
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchall()	
	statelist = []
	for entry in dbinfo: statelist.append( entry)
	
	
	totalseats = 0
	democratlosses = 0

	for state in statelist:

		sql_cmd = "SELECT rankings.month, rankings.dayofmonth, rankings.dem, rankings.rep, rankings.indep, statetable.abrev, rankings.indep, candidate_names.incumbentparty from rankings left join statetable on rankings.state = statetable.fullname\
		 left join candidate_names on statetable.abrev = candidate_names.state where  statetable.abrev = '%s' " % state
		cursor.execute(sql_cmd)
		dbinfo = cursor.fetchall()
		
		datalist = [ ]
	
		for entry in dbinfo: datalist.append(entry)
		if datalist != []:
			datalist.sort(key = lambda x: x[1],reverse = True)
			datalist.sort(key = lambda x: x[0], reverse = True)
			
			totalseats += 1
			if (datalist[0][2] <  datalist[0][3] ) or (datalist[0][2]< int(datalist[0][4])):
				democratlosses += 1

	print "Dems expected to lose %i of %i elections"% (democratlosses, totalseats)





#Q6: PLOTS polling data for a given state
def q6():
	'''#Q6: PLOTS polling data for a given state'''
	#get STATE; connect to db
	state = raw_input('enter a 2digit state code to see a plot:').upper()
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	
	#query db, get names, rankings for Rep, Dem, Ind candidates
	sql_cmd = "SELECT candidate_names.democrat, candidate_names.republican, candidate_names.independent, rankings.day, rankings.dem, rankings.rep, rankings.indep from rankings left join statetable on rankings.state = statetable.fullname\
	 left join candidate_names on statetable.abrev = candidate_names.state where  statetable.abrev = '%s' order by rankings.day ASC" % state
	cursor.execute(sql_cmd)
	dbinfo = cursor.fetchall()

	#'new' is the name of the record array corresponding to the output from the sql query
	new = N.array(dbinfo, dtype= [('demname', '|S25'),('repname', '|S25'),('indname', '|S25'),('day', N.int16), ("dem", N.int16), ("rep", N.int16), ("ind", N.int16)])

	demname= new['demname'][0] #name of democrat
	repname=  new['repname'][0] # name of rep
	indname= new['indname'][0] #" of ind

	# 2 (+1) lines for dem, rep, candiates ind if he has more than 1 point at the first datapoint, indicating there is an independent candidate
	plt.plot(new['day'],new['dem'], color='blue', label='%s' % demname)
	plt.plot(new['day'],new['rep'], color='red', label='%s' % repname)
	if new['ind'][0] > 1:
		plt.plot(new['day'],new['ind'], color='green', label='%s' % indname)
		
	#plot info
	plt.suptitle('Election Polls for the State of %s'%state)
	plt.xlabel('Day of the year')
	plt.ylabel('Points')
	plt.legend()
	plt.show()



#This FUNCTION allows one to enter new polling data into the table, ratings
# enterData(day, dem, rep, month, dayofmonth, len=0, indep=0, fullstate = 'California',poll='unknown')
#all of the  parameters are ints except poll and fullstate, which are strings
# do not enter abreviations for fullstate

def enterData(day, dem, rep, month, dayofmonth, len=0, indep=0, fullstate = 'California',poll='unknown'):
	'''#This FUNCTION allows one to enter new polling data into the table, ratings
	# enterData(day, dem, rep, month, dayofmonth, len=0, indep=0, fullstate = 'California',poll='unknown')
	#all of the  parameters are ints except poll and fullstate, which are strings
	# do not enter abreviations for fullstate'''
	connection = sqlite3.connect(path+"/poll.db")
	cursor = connection.cursor()
	cmd = 'INSERT INTO rankings (day, len, dem, rep, indep, month, dayofmonth, state,poll) VALUES (%i, %i, %i, %i, %i,%i, %i, "%s","%s")'%(day, len, dem, rep, indep, month, dayofmonth, fullstate.upper(),poll.upper()) 
	cursor.execute(cmd)
	connection.commit()
	connection.close()
	

	
		