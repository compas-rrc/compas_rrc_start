from compas_rrc import *
from compas_fab.backends.ros import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = AbbClient(ros, '/rob1')
    print('Connected.')

    # Set tool
    done = abb.send_and_wait(SetTool('tool0'))

    # Set work object
    done = abb.send_and_wait(SetWorkObject('wobj0'))

    # Set acceleration
    acc = 100 # Unit [%]
    ramp = 100  # Unit [%]
    done = abb.send_and_wait(SetAcceleration(acc, ramp))

    # Set max speed
    override = 100 # Unit [%]
    max_tcp = 2500 # Unit [mm/s]
    done = abb.send_and_wait(SetMaxSpeed(override, max_tcp))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
