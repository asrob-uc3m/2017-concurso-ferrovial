#! /usr/bin/env python

import time as t

import yarp
import rd

def main():

    left_threshold = 0 #  Edit this with sensor values
    center_threshold = 0  # Edit this with sensor values
    right_threshold = 0  # Edit this with sensor values

    yarp.Network.init()

    if yarp.Network.checkNetwork() != True:
        print "[error] Please try running yarp server"
        quit()

    robotOptions = yarp.Property()
    robotOptions.put('device','RobotClient')
    robotOptions.put('name','/RobotServer')
    robotDevice = yarp.PolyDriver(robotOptions)  # calls open -> connects

    robot = rd.viewRdRobotManager(robotDevice)  # view the actual interface

    #######
    try:

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.turnLeft(20)
        yarp.Time.delay(0.2)  # 90 degrees

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.turnRight(20)
        yarp.Time.delay(0.2)  # 90 degrees

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.turnRight(20)
        yarp.Time.delay(0.2)  # 90 degrees

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

 #       robot.turnLeft(20)
 #       yarp.Time.delay(0.2)  # 90 degrees

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

        robot.moveForward(20)
        yarp.Time.delay(3.3)  # 1 m = 3.3

        robot.stopMovement() # optional
        yarp.Time.delay(0.1) 

#        robot.turnLeft(20)
#        yarp.Time.delay(0.4)  # 90 degrees

        robot.stopMovement()

    except KeyboardInterrupt:
        robot.stopMovement()
        robotDevice.close()

    ######
    robot.stopMovement()
    robotDevice.close()

if __name__ == '__main__':
    main()

