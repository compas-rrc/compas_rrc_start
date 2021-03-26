import compas_rrc as rrc
from compas.geometry import Frame 
from compas.geometry import Point
from compas.geometry import Vector

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Define robot joints
    robot_joints_start_position = [0.0, -20.0, 40.0, 0.0, -20.0, 0.0]
    robot_joints_end_position = [0.0, -30.0, 50.0, 0.0, -20.0, 0.0]

    # Define print frames x 
    frame_print_start_X = Frame(Point(750.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
    frame_print_end_X = Frame(Point(250.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

    # Define print frames x
    frame_print_start_Y = Frame(Point(750.000, 350.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
    frame_print_end_Y = Frame(Point(250.000, 350.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

    # Define print frames x
    frame_print_start_Z = Frame(Point(750.000, 450.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
    frame_print_end_Z = Frame(Point(250.000, 450.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

    # Define external axis
    external_axis_dummy = []

    # Select tool and print output
    print_tool = 't_RRC_Tool_Z'
    print_signal = 'do_Z'

    # Select print path
    frame_print_start = frame_print_start_Z
    frame_print_end = frame_print_end_Z

    # Define speed 
    speed = 800
    speed_print = 150 

    # Set Acceleration
    acc = 100  # Unit [%]
    ramp = 100  # Unit [%]
    abb.send(rrc.SetAcceleration(acc, ramp))

    # Set Max Speed
    override = 100  # Unit [%]
    max_tcp = 2500  # Unit [mm/s]
    abb.send(rrc.SetMaxSpeed(override, max_tcp))

    # Reset signals 
    abb.send(rrc.SetDigital('do_X',0))
    abb.send(rrc.SetDigital('do_Y',0))
    abb.send(rrc.SetDigital('do_Z',0))

    # Set tool
    abb.send(rrc.SetTool(print_tool))

    # Set work object
    abb.send(rrc.SetWorkObject('ob_RRC_Workplace'))

    # User message -> basic settings send to robot
    print('Tool, Wobj, Acc and MaxSpeed sent to robot')

    # Stop task user must press play button on the FlexPendant (RobotStudio) before robot starts to move
    abb.send(rrc.PrintText('Press Play to move.'))
    abb.send(rrc.Stop())

    # Move robot to start position
    done = abb.send_and_wait(rrc.MoveToJoints(robot_joints_start_position, external_axis_dummy, speed, rrc.Zone.FINE))

    # User message and input
    input('Robot start position reached, press any key to start the print.')

    # Move to print start
    abb.send(rrc.MoveToFrame(frame_print_start, speed, rrc.Zone.FINE))

    # Start watch
    done = abb.send_and_wait(rrc.StartWatch())

    # Start print
    abb.send(rrc.SetDigital(print_signal, 1))

    # Print path
    abb.send(rrc.MoveToFrame(frame_print_end, speed_print, rrc.Zone.FINE, rrc.Motion.LINEAR))

    # End print
    abb.send(rrc.SetDigital(print_signal, 0))

    # Stop watch
    done = abb.send_and_wait(rrc.StopWatch())

    # Read watch
    future = abb.send(rrc.ReadWatch())

    # Move robot to end position
    abb.send(rrc.MoveToJoints(robot_joints_end_position, external_axis_dummy, speed, rrc.Zone.FINE))

    # Read and print printing time
    watch_time = future.result(timeout=3.0)
    print('Print Time [s] = ', watch_time)

    # Print Text
    done = abb.send_and_wait(rrc.PrintText('Compas_RRC Example finish.'))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
