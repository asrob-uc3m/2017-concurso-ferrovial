
import yarp

import numpy

import matplotlib.pylab

yarp_width = 320
yarp_height = 240

yarp.Network.init()

input_port = yarp.Port()
input_port.open("/python/depth:i");

if yarp.Network.connect("/OpenNI2/depthFrame:o", "/python/depth:i") != True:
    print "[error] Could not connect"
    quit()

#while(1):

# Create numpy array to receive the image and the YARP image wrapped around it
img_array = numpy.zeros(( yarp_height , yarp_width ), dtype=numpy.uint16)
yarp_image = yarp.ImageMono16()
yarp_image.resize( yarp_width , yarp_height )
yarp_image.setExternal(img_array, img_array.shape[1], img_array.shape[0])
# Read the data from the port into the image
input_port.read(yarp_image)
if yarp_image.getRawImage().__long__() <> img_array.__array_interface__['data'][0]:
        print "read() reallocated my yarp_image!"

print "good up to here"
# display the image that has been read
matplotlib.pylab.imshow(img_array,interpolation='none')
matplotlib.pylab.show()

#puntoIzquierda = yarp_depth.getPixel(100,430) # for 640x480
#puntoCentro = yarp_depth.getPixel(340,430)
#puntoDerecha = yarp_depth.getPixel(580,430)
#print str(puntoIzquierda) + " " + str(puntoCentro) + " " + str(puntoDerecha)

input_port.close()

yarp.Network.fini()

