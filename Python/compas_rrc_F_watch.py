from compas_rrc import *
from compas_fab.backends.ros import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = AbbClient(ros, '/rob1')
    print('Connected.')

    # Switches for Code
    on = True
    off = False

    # Start watch
    done = abb.send_and_wait(StartWatch())

    # Stop watch
    done = abb.send_and_wait(StopWatch())

    # Read watch
    watch_time = abb.send_and_wait(ReadWatch()) # Unit [s]

    # Print current time
    print(watch_time)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
