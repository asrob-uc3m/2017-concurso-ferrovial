// -*- mode:C++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-

#ifndef __EXAMPLE_PROGRAM_HPP__
#define __EXAMPLE_PROGRAM_HPP__

#include <yarp/os/all.h>
#include <yarp/sig/all.h>

namespace teo
{

/**
 * @ingroup exampleProgram
 *
 * @brief exampleProgram
 *
 */
class ExampleProgram : public yarp::os::RFModule
{
    public:
        /** Runs on open() **/
        bool configure(yarp::os::ResourceFinder &rf);

    private:
        // Ports
        yarp::os::BufferedPort<yarp::sig::ImageOf<yarp::sig::PixelFloat> > inPort;

        // RFModule
        virtual bool interruptModule();
        virtual double getPeriod();
        virtual bool updateModule();

};

}  // namespace teo

#endif  // __EXAMPLE_PROGRAM_HPP__
