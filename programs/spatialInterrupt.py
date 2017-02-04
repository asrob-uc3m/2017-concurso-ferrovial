import yarp

normal_speed = 20
high_speed = 15
low_speed = 30
speed = normal_speed

yarp.Network.init()

class DataProcessor(yarp.PortReader):
    def read(self,connection):
        #print("in DataProcessor.read")
        if not(connection.isValid()):
            print("Connection shutting down")
            return False
        bin = yarp.Bottle()
        #print("Trying to read from connection")
        ok = bin.read(connection)
        if not(ok):
            print("Failed to read input")
            return False
	angle = bin.get(0).asDouble()
	#print angle
	global speed
	if angle > 100:
	    speed = high_speed
	elif angle < 80:
	    speed = low_speed
	else:
	    speed = normal_speed
	return True
#        bout = yarp.Bottle()
#        print("Received [%s]"%bin.toString())
#        bout.addString("Received:")
#        bout.append(bin)
#        print("Sending [%s]"%bout.toString())
#        writer = connection.getWriter()
#        if writer==None:
#            print("No one to reply to")
#            return True
#        return bout.write(writer)

p = yarp.Port()
r = DataProcessor()
p.setReader(r)
p.open("/python/spatial:i");

while(1):

    print speed
    yarp.Time.delay(1)

p.close();

yarp.Network.fini();

