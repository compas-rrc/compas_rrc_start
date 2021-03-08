import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # ==============================================================================
    # SEND
    # ==============================================================================

    # User agtion
    input('Press enter to execute the send command.')

    # Send
    abb.send(rrc.PrintText('Send instructions to the robot.'))
  
    # ==============================================================================
    # SEND AND WAIT
    # ==============================================================================

    # User agtion
    input('Press enter to execute the send and wait command.')

    # Send and wait
    done = abb.send_and_wait(rrc.PrintText('Send instructions to the robot and wait for feedack.'))

    # Print feedback
    print('Feedback = ', done)

    # ==============================================================================
    # SEND AND WAIT IN THE FUTURE
    # ==============================================================================

    # User agtion
    input('Press enter to execute the send and wait in the future command.')

    # Send and wait in the futer
    future = abb.send(rrc.PrintText('Send instructions to the robot and check the feedack later.',feedback_level=1))

    # Execute other code 
    print('Execute other code.')

    # Wait for future feedback
    done = future.result(timeout=3.0)

    # Print feedback
    print('Future Feedback = ', done)

    # ==============================================================================
    # SEND AND SUBSCRIBE
    # ==============================================================================

    # Send and subscribe
    # This feature is currently only usable with custom instructions.

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
