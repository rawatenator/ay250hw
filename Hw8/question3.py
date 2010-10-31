import os
import sys

# Download the latest polling data 
# from http://electoral-vote.com/evp2010/Senate/ 
# senate_polls.raw (or .csv) into your Week 8 homework folder.
  
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


relative_path_to_module = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.abspath(relative_path_to_module))

print sys.path

from Hw5.Hw5 import *
print 1