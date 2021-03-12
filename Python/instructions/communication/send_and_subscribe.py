import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Send and subscribe
    # This feature is currently only usable with custom instructions.

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
