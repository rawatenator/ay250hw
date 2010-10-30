
##1) Form pairs to write XML-RPC server/client programs (one student 
##writes each).

# I am working with James Long


##• The server offers 3 methods providing lossless image manipulation 
##(be creative). Each server method must have descriptive 
##documentation accessible by the client. 



#import stuff
import SimpleXMLRPCServer
import numpy as np
from pylab import imread, gray, mean
import scipy as sp
from matplotlib import pyplot
from PIL import Image
import ImageFilter


# Set IP/PORT SPECIFICS:
host, port = "68.183.197.83", 2000



#make manipulationclass
class Image_Manipulation_Class:
    i = 0  #i is a counter
    
    
    def rotate180(self, listed_Stuff,modeofpic = 'RGB'):
        '''
        function works on a list, which can be made by using the .tolist()
        method on a numpy array. function returns a list corresponding to
        a modified image. It can be made back into an array using np.array(list)

        PIL is used to do modifications.

        rotate180 uses the PIL mthd Image.rotate(180)

        Copies of the original and modified images will storred on the server'''
        #make the array from list
        array_from_list = np.array(listed_Stuff, dtype = np.uint8)

        #make an Image obj from the array
        starting_Img = Image.fromarray(array_from_list, mode = modeofpic)

        #save the starting image
        starting_Img.save("/%s_%i.png" % ("starting_Image", Image_Manipulation_Class.i) )

        #perform manipulation, call manipulated img final_Img
        final_Img = starting_Img.rotate(180)
        
        #save final_Img, increment the counter, 
        final_Img.save("/%s_%i.png" % ("final_Image", Image_Manipulation_Class.i) )
        Image_Manipulation_Class.i += 1

        #make a list from the final img object, return it
        arrayFinal = np.array(final_Img)
        lisFinal = arrayFinal.tolist()
        return lisFinal
    
    def flipLeftRight(self, listed_Stuff,modeofpic = 'RGB'):
        '''
        function works on a list, which can be made by using the .tolist()
        method on a numpy array. function returns a list corresponding to
        a modified image. It can be made back into an array using np.array(list)

        PIL is used to do modifications.

        rotate180 uses the PIL mthd Image.FLIP_LEFT_RIGHT

        Copies of the original and modified images will storred on the server'''
        
        #make the array from list
        array_from_list = np.array(listed_Stuff, dtype = np.uint8)

        #make an Image obj from the array
        starting_Img = Image.fromarray(array_from_list, mode = modeofpic)

        #save the starting image
        starting_Img.save("/%s_%i.png" % ("starting_Image", Image_Manipulation_Class.i) )

        #perform manipulation, call manipulated img final_Img
        final_Img = starting_Img.transpose(Image.FLIP_LEFT_RIGHT)

        
        #save final_Img, increment the counter, 
        final_Img.save("/%s_%i.png" % ("final_Image", Image_Manipulation_Class.i) )
        Image_Manipulation_Class.i += 1

        #make a list from the final img object, return it
        arrayFinal = np.array(final_Img)
        lisFinal = arrayFinal.tolist()
        return lisFinal

    def flipTopBot(self, listed_Stuff,modeofpic = 'RGB'):
        '''
        function works on a list, which can be made by using the .tolist()
        method on a numpy array. function returns a list corresponding to
        a modified image. It can be made back into an array using np.array(list)

        PIL is used to do modifications.

        rotate180 uses the PIL mthd Image.FLIP_TOP_BOTTOM

        Copies of the original and modified images will storred on the server'''

        #make the array from list
        array_from_list = np.array(listed_Stuff, dtype = np.uint8)

        #make an Image obj from the array
        starting_Img = Image.fromarray(array_from_list, mode = modeofpic)

        #save the starting image
        starting_Img.save("/%s_%i.png" % ("starting_Image", Image_Manipulation_Class.i) )

        #perform manipulation, call manipulated img final_Img
        final_Img = starting_Img.transpose(Image.FLIP_TOP_BOTTOM)

        
        #save final_Img, increment the counter, 
        final_Img.save("/%s_%i.png" % ("final_Image", Image_Manipulation_Class.i) )
        Image_Manipulation_Class.i += 1

        #make a list from the final img object, return it
        arrayFinal = np.array(final_Img)
        lisFinal = arrayFinal.tolist()
        return lisFinal





#activate the server:
server = SimpleXMLRPCServer.SimpleXMLRPCServer((host, port),allow_none=True) 
server.register_instance(Image_Manipulation_Class()) 
server.register_introspection_functions() 
print "XMLRPC Server is starting at:", host, port 
server.serve_forever() 
















##• The client calls each method on the server machine with an array 
##from an image. The client must then reverse the server methods to 
##recover the original image.
##•Client saves the original image, modified image received from the 
##server, and then reconstructed image. Server saves image received 
##from the client and modified image. 



#done by client, I am server



##•Include example images in your solutions, and note your partner in 
##your README. Do not discuss the nature of the server methods 
##outside of the in-line documentation (client author can pester server 
##author for more explicit documentation if it is not adequate).
