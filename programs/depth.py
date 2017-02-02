import yarp

yarp.Network.init()

p = yarp.Port()
p.open("/depth:i");

if yarp.Network.connect("/OpenNI2/depthFrame:o", "/depth:i") != True:
    print "[error] Could not connect"
    quit()

while(1):

    yarp_depth = yarp.ImageMono16()
    p.read(yarp_depth)

    puntoIzquierda = yarp_depth.getPixel(100,430)
    puntoCentro = yarp_depth.getPixel(340,430)
    puntoDerecha = yarp_depth.getPixel(580,430)

    print str(puntoIzquierda) + " " + str(puntoCentro) + " " + str(puntoDerecha)

p.close();

yarp.Network.fini();

