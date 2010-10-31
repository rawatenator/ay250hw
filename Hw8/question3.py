#import stuff/set sys.path for Hw5.Hw5
import os
import sys
relative_path_to_module = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.abspath(relative_path_to_module))
from Hw5.Hw5 import *

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

