import compas_rrc as rrc
from compas_fab.backends import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    result = abb.send_and_wait(rrc.PrintText('Welcome to COMPAS_RRC'))
    print(result)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
