import yarp

speed = 20

yarp.Network.init()

while(1):

    print speed
    yarp.Time.delay(1)

p.close();

yarp.Network.fini();

