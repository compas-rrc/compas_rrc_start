import compas_rrc as rrc
from compas_fab.backends import RosClient

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

    # Print text
    done = abb.send_and_wait(PrintText('The Task T_Rob1 will stop in 1 second!'))

    # Wait time
    time = 1.0
    done = abb.send_and_wait(WaitTime(time))

    # Stop
    done = abb.send_and_wait(Stop())

    # Noop
    done = abb.send_and_wait(Noop())

    # Custom instruction
    string_values = ['Custom Text']
    float_values = [42]
    done = abb.send_and_wait(CustomInstruction('r_RRC_CustomInstruction', string_values, float_values))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
