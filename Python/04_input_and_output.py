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

    # Read and set analog
    if on:

        # Read analog
        analog_input_1 = abb.send_and_wait(ReadAnalog('ai_1'))

        # Print current value
        print(round(analog_input_1, 2))

        # Set analog output
        value = -3.33
        done = abb.send_and_wait(SetAnalog('ao_1', value))

    # Read and set digital
    if on:

        # Read digital
        digital_input_1 = abb.send_and_wait(ReadDigital('di_1'))

        # Print current value
        print(digital_input_1)

        # Set digital output to low or high
        low = 0
        high = 1
        done = abb.send_and_wait(SetDigital('do_1',low))

    # Pulse digitals
    if on:

        # Pulse digital output 
        pulse_time = 2.5 # Unit [s]
        done = abb.send_and_wait(PulseDigital('do_1', pulse_time))

    # Read and set group
    if on:

        # Read group
        group_input_1 = abb.send_and_wait(ReadGroup('gi_1'))

        # Print current value
        print(group_input_1)

        # Set group output
        value = 33
        done = abb.send_and_wait(SetGroup('go_1', value))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
