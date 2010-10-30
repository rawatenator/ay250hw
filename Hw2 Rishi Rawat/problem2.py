import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mp



#open png with matplotlib.image
img=mpimg.imread('flower.png')

#new figure, show input img
plt.figure()
plt.imshow(img)




# do fourier transform


fourier = np.fft.fft2(img)


power = abs(fourier)# clip based on the 95th percentile: mp.mlab.prctile(power,95)
powerclip = power.clip(min=0,max=121)


plt.figure()
plt.imshow(powerclip)

plt.colorbar()






# filter the spectrum

rows, columns = np.shape(fourier)#tells us there are (474, 630) rows, columns
frac = .1 #how much lowfrequency data to keep; same for col/rows
filtered = fourier.copy() #make copy to avoid messing up orig. data

filtered[70: -70] = 0 #rows
filtered[:,60: -60] = 0  #columns


plt.figure()
plt.imshow(abs(filtered).clip(min=0,max=121), label="filtered")


##
####
##### do inverse tranform
inverse =(np.fft.ifft2(filtered)).real
plt.figure()
plt.imshow(inverse)
plt.show()
