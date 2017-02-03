yarpview --name /yarpview/depth:i     &
sleep 1
yarp connect /OpenNI2/depthFrame:o /yarpview/depth:i
