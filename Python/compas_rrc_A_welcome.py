from compas_rrc import *
from compas_fab.backends.ros import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = AbbClient(ros, '/rob1')
    print('Connected.')

    # Test compas_rrc  
    result = abb.send_and_wait(PrintText('Welcome to COMPAS_RRC'))
    print(result)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
