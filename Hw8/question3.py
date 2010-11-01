#import stuff/set sys.path for Hw5.Hw5
import os
import sys
relative_path_to_mod = os.path.join(os.path.dirname(__file__), '..')
abs_path_to_mod = os.path.abspath(relative_path_to_mod)
sys.path.append(abs_path_to_mod)
import Hw5.Hw5
from Hw5.Hw5 import q1 as add_senate_polls_data_to_db
import datetime


today = datetime.date.today()


#these functions initialize the database poll.db(in the hw5 directory), the last function
#is responsible for getting the new polling data into the database

#Hw5.Hw5.q0()
#Hw5.Hw5.q2()
#Hw5.Hw5.q3()
#add_senate_polls_data_to_db(os.path.abspath(os.path.join(os.path.dirname(__file__), 'senate_polls_recent.csv')))




#to test if the new data is in the database, enable the following function: then enter a statename and see a
#webpage with the latest polling data

#Hw5.Hw5.q4()


import argparse
parser = argparse.ArgumentParser(description='Polldata') 

parser.add_argument('-graph', action='store_true',
					help='by adding this keywork, a the graph of the state polling #s will be displayed', default = False)					
parser.add_argument('-add', action='store_true',
					help='by adding this keywork, you can enter data into the database. simply add the other keywords with relevant data and the information will be added. If -graph is also a keyword, the grpah will be made after the new entry is made', default = False)

parser.add_argument('-day', action='store', dest = 'day_in_cycle',
                    help='Store the day in the election cycle e.g. 234th day in the cycle; default:0', default=today.timetuple()[7] )
parser.add_argument('-dem', action='store', dest = 'dem',
                    help='dem candidate"s points; default:0', default=0)
parser.add_argument('-rep', action='store', dest = 'rep',
                    help='republican candiate"s points; default:0', default=0)
parser.add_argument('-ind', action='store', dest = 'ind',
                    help='independent candiate"s points; default:0', default=0)
parser.add_argument('-m', action='store', dest = 'month',
                    help='month of poll e.g. 1 - 12', default=today.month)
parser.add_argument('-d', action='store', dest = 'day',
                    help='day of poll eg 4 for July 4th', default=today.day)
parser.add_argument('-state', action='store', dest = 'state',
					help='full name of state(e.g., California)', default = 'California')
parser.add_argument('-poll', action='store', dest = 'poll',
					help='name of the polling company', default = 'unknown')

					
res = parser.parse_args()

print res

if res.add:
	day = int(res.day_in_cycle)
	dem = int(res.dem)
	rep = int(res.rep)
	month = int(res.month)
	dayofmonth = int(res.day)
	indep = int(res.ind)
	fullstate = res.state.upper()
	poll = res.poll
		
	
	Hw5.Hw5.enterData(day, dem, rep, month, dayofmonth, len=0, indep=indep, fullstate = fullstate,poll= poll)
	print "data entered successfully"


	if res.graph == False:
		print 'to graph the data of the state you just entered try running the program with the kwrds '
		print '-graph -state '+ state
		
if res.graph:
	state_abreviation = Hw5.Hw5.getabrevfromfull(res.state.upper())
	
	Hw5.Hw5.q6(state_abreviation)
	
	
# Download the latest polling data 
# from http://electoral-vote.com/evp2010/Senate/ 
# senate_polls.raw (or .csv) into your Week 8 homework folder.
#-Done
  
# Without moving the base code from your Week 5 (databases) 
# folder*, load the necessary functions from that code into a new 
# module.

#which parses command-line 
# input using argparse.  

#Allow the user to input new polls into 
# the database without requiring a specific format  

#Include an option which shows a plot of the updated polls for a given 
# state.  

#Include the necessary checks to make sure the user's 
# path is set correctly to import the code from Week 5. 

