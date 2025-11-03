import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Send and wait in the futer
    future = abb.send(rrc.PrintText('Send instructions to the robot and check the feedack later.',feedback_level=1))

    # Execute other code 
    print('Execute other code.')

    # Wait for future feedback
    done = future.result(timeout=3.0)

    # Print feedback
    print('Future Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
