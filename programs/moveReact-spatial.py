
import yarp
import rd

import numpy

#import matplotlib.pylab

import operator

yarp_width = 320
yarp_height = 240

yarp.Network.init()

input_port = yarp.Port()
input_port.open("/python/depth:i");

if yarp.Network.connect("/OpenNI2/depthFrame:o", "/python/depth:i") != True:
    print "[error] Could not connect"
    quit()

robotOptions = yarp.Property()
robotOptions.put('device','RobotClient')
robotOptions.put('name','/RobotServer')
robotDevice = yarp.PolyDriver(robotOptions)  # calls open -> connects

robot = rd.viewRdRobotManager(robotDevice)  # view the actual interface

while(1):
    yarp.Time.delay(0.5)
    # Create numpy array to receive the image and the YARP image wrapped around it
    img_array = numpy.zeros(( yarp_height , yarp_width ), dtype=numpy.uint16)
    yarp_image = yarp.ImageMono16()
    yarp_image.resize( yarp_width , yarp_height )
    yarp_image.setExternal(img_array, img_array.shape[1], img_array.shape[0])
    # Read the data from the port into the image
    input_port.read(yarp_image)
    if yarp_image.getRawImage().__long__() <> img_array.__array_interface__['data'][0]:
        print "read() reallocated my yarp_image!"

    #print "good up to here"
    # display the image that has been read
    #matplotlib.pylab.imshow(img_array,interpolation='none')
    #matplotlib.pylab.show()

    # 170 = (17/24) * 240 = (17/24) * yarp_height
    down_puntoIzquierda = img_array[  (17.0/24.0) * yarp_height , 45  ]   
    down_puntoCentro = img_array[ (17.0/24.0) * yarp_height , 187 ]  
    down_puntoDerecha = img_array[ (17.0/24.0) * yarp_height , 285  ]
    print str(down_puntoIzquierda) + " " + str(down_puntoCentro) + " " + str(down_puntoDerecha)

    if (down_puntoDerecha < 700) or (down_puntoDerecha == 0):
            print "left"
            robot.turnLeft(20)
            yarp.Time.delay(0.2)  # 90 degrees
            robot.stopMovement() # optional
            robot.moveForward(20)
            yarp.Time.delay(0.2)  # 90 degrees
            robot.stopMovement() # optional
    elif (down_puntoIzquierda < 700) or (down_puntoIzquierda == 0):
            print "right"
            robot.turnRight(20)
            yarp.Time.delay(0.2)  # 1 m = 3.3
            robot.stopMovement() # optional
            robot.moveForward(20)
            yarp.Time.delay(0.2)  # 90 degrees
            robot.stopMovement() # optional
    elif down_puntoCentro == 0:
            print "back and left"
            robot.moveBackwards(20)
            yarp.Time.delay(0.2)  # 90 degrees
            robot.stopMovement() # optional
            yarp.Time.delay(0.2)  # 90 degrees
            robot.turnLeft(20)
            yarp.Time.delay(0.2)  # 90 degrees
            robot.stopMovement() # optional
    elif down_puntoCentro > 2000:
            print "big left"
            robot.turnLeft(20)
            yarp.Time.delay(0.8)  # 90 degrees
            robot.stopMovement() # optional
            robot.moveForward(20)
            yarp.Time.delay(0.2)  # 90 degrees
    else:
            print "advance"
            robot.moveForward(20)
            yarp.Time.delay(0.5)  # 90 degrees
            robot.stopMovement() # optional
    #puntoIzquierda = yarp_depth.getPixel(100,430) # for 640x480
    #puntoCentro = yarp_depth.getPixel(340,430)
    #puntoDerecha = yarp_depth.getPixel(580,430)
    #print str(puntoIzquierda) + " " + str(puntoCentro) + " " + str(puntoDerecha)

input_port.close()

yarp.Network.fini()

