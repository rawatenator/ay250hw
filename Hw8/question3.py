#import stuff/set sys.path for Hw5.Hw5
import os
import sys
relative_path_to_mod = os.path.join(os.path.dirname(__file__), '..')
abs_path_to_mod = os.path.abspath(relative_path_to_mod)
sys.path.append(abs_path_to_mod)
import Hw5.Hw5
from Hw5.Hw5 import q1 as add_senate_polls_data_to_db


#these functions initialize the database poll.db(in the hw5 directory), the last function
#is responsible for getting the new polling data into the database

#Hw5.Hw5.q0()
#Hw5.Hw5.q2()
#Hw5.Hw5.q3()
#add_senate_polls_data_to_db(os.path.abspath(os.path.join(os.path.dirname(__file__), 'senate_polls_recent.csv')))




#to test if the new data is in the database, enable the following function: then enter a statename and see a
#webpage with the latest polling data

#Hw5.Hw5.q4()

 

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

