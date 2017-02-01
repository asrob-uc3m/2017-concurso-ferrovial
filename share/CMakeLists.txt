# Copyright: UC3M 2017
# Author: ASROB UC3M Team
# CopyPolicy: Released under the terms of the GNU GPL v2.0.
# 

find_package(YARP REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
include(YarpInstallationHelpers)
yarp_configure_external_installation(2017-concurso-ferrovial)

### Go through single applications

#add_subdirectory(prog)

