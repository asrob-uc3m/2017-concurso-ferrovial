yarpview --name /yarpview/rgb:i     &
sleep 1
yarp connect /OpenNI2/imageFrame:o /yarpview/rgb:i
