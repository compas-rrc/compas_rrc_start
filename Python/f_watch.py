import compas_rrc as rrc
from compas_fab.backends import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = AbbClient(ros, '/rob1')
    print('Connected.')

    # Start watch in robot controller 
    done = abb.send_and_wait(StartWatch())

    # Stop watch in robot controller 
    done = abb.send_and_wait(StopWatch())

    # Read time from watch in robot controller 
    watch_time = abb.send_and_wait(ReadWatch()) # Unit [s]

    # Print robot watch time
    print(watch_time)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
