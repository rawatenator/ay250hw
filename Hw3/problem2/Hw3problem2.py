#HW3 problem 2 by RISHI RAWAT
#import stuff:

import pyaudio
import aifc
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
import struct
import scipy, math
name = raw_input("enter a filename, but not the .aif part:")


#ask the user to choose an audiofile
filename = "%s.aif"%name
audio = aifc.open("sound_files/%s" % filename, "r")


#set variables for audio characteristics:
Frate =  audio.getframerate(), #"Hz sampling rate"
Frames = audio.getnframes() #total number of frames
width = audio.getsampwidth() 
channels = audio.getnchannels()




###GET THEN UNPACK THE DATA
# I strugggled a lot with unpacking the data and ended up using techniques from Alex Robinson to unpack and split channels
#from: http://bugs.python.org/issue4913

data =  audio.readframes(Frames) 

data2 = struct.unpack("<%uh" % (len(data) / width), data) #now in base 16


# deal with the channels:
datastructure= []
if channels >1:
	for i in xrange(channels):
		datastructure.append([ data2[audiobit] for audiobit in xrange(0,len(data2),channels)])
else:
	datastructure = [data2]
	





#make one fig, w/2 plots. THE FIRST SUBPLOT IS THE SOUNDWAVE:


plt.figure(1)
plt.subplot(211)

#Y - AXIS
yval = np.array(datastructure[0]) #DATASTRUCTURE[0] IS REFERRING TO THE DATA CONTAINED IN ONE PARTICULAR CHANNEL, 0

#X - AXIS
#MAKE AN ARRAY FOR TIME POINTS
timeArray = np.arange(0, Frames, 1)
timeArray = timeArray / Frate[0] #in seconds
timeArray = scipy.linspace(0,Frames / Frate[0],Frames)

#PLOT
plt.plot(timeArray, yval)
plt.ylabel('Amplitude')
plt.xlabel('time, in sec')






####
#THE SECOND SUBPLOT IS THE FFT POWER SPECTRUM

#do fft on first channel:
array = np.array(datastructure[0])
fft = np.fft.fft(array)


##### I HAVE NO EXPERIENCE DOING FFT, SO MANY OF THE FOLLOWING CALCULATIONS WERE MADE AFTER CONSULTING 
##### http://xoomer.virgilio.it/sam_psy/psych/sound_proc/sound_proc_python.html
##### SOME OF THE DATA MANIPULTIONS WERE CARRIED OUT IN EXACTLY THE SAME WAY


n = len(datastructure[0]) 
nUniquePts = math.ceil((n+1)/2.0)
p = fft[0:nUniquePts]  #b/c fft is unique for only half of the columns
p = abs(p)
p = p / float(n) # so the specturm isn't swayed by length of sound
p = p**2 # to make large values stand out




# directly from the site, so that there are an equal num of pts in the fourier tranform and in the following freqArray array. Works with the ceil for nUniquePts
if n % 2 > 0:
    p[1:len(p)] = p[1:len(p)] * 2
else:
	p[1:len(p) -1] = p[1:len(p) - 1] * 2


plt.subplot(212)
freqArray = np.arange(0.0000000000000000000000000001, nUniquePts, 1.0)*(Frate[0] / float(n));
yArray = 10. * np.log10(p)

plt.plot(freqArray,yArray , color='k')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.xlim((200, 1000))
plt.ylim((20,50))









#
#TO MAKE FILE ANALYSIS EASIER, THIS METHOD PRINTS OUT PTS WHICH HAVE LARGE POWER SCORES
def idmax(low=0.,high=1000.):
	limit = mp.mlab.prctile(yArray[low:high,],100.1)
	for i in xrange(freqArray.shape[0]):
		if freqArray[i]<low:
			continue
		if freqArray[i]>high:
			break
		if yArray[i,] > limit:
			print freqArray[i,], yArray[i]


#RUN THE METHOD			
idmax()

#SHOW THE GRAPH
plt.suptitle("%s"%filename)
plt.savefig("soundfigures/%s.png"%filename)
plt.show()




#TO MAKE DATA ENTRY EASY AND EFFICIENT, THE PROGRAM APPENDS A FILE CALLED SOUNDNOTES.DAT, WHICH CONTAINS USER
#INPUTTED DATA ABOUT THE MOST DOMINANT FREQUENEIS AND THIER RELATIVE POWER SCORES

datafile = open('soundfigures/soundnotes.dat','a')
while True:
	highfreq = raw_input("enter freq w/high powers. like: frequency,power; TYPE q TO END")
	if highfreq is 'q':
		
		datafile.write("\n")
		datafile.close()
		break
	else: 
		freq,power = highfreq.split(',')
		datafile.write("%s \t\t\t\t freq: %s power: %s\n"%(filename, freq, power) )
		continue

