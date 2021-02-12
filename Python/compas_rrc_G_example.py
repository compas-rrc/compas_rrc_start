from compas_rrc import *
from compas.geometry import Frame, Point, Vector
from compas_fab.backends.ros import RosClient

if __name__ == '__main__':

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Create ABB Client
    abb = AbbClient(ros, '/rob1')
    print('Connected.')

    # Set Tool
    abb.send(SetTool('t_X000_Tool_X'))

    # Set Work Object
    abb.send(SetWorkObject('ob_X000_Workplace'))

    # Set Acceleration
    acc = 100  # Unit [%]
    ramp = 100  # Unit [%]
    abb.send(SetAcceleration(acc, ramp))

    # Set Max Speed
    override = 100  # Unit [%]
    max_tcp = 250  # Unit [mm/s]
    abb.send(SetMaxSpeed(override, max_tcp))

    # User message -> basic settings send to robot
    print('Tool, Wobj, Acc and MaxSpeed sent to robot')

    # Define robot joints
    robot_joints_start_position = [0.0, -7.34, 36.02, 180.0, 28.68, 180.0]
    robot_joints_end_position = [0.0, -17.34, 46.02, 180.0, 28.68, 180.0]

    # Define external axis
    external_axis_dummy = []

    # Define frames
    frame_print_start = Frame(Point(750.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
    frame_print_end = Frame(Point(250.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

    # Stop task user must press play button before robot starts to move
    abb.send(PrintText('Press Play to move.'))
    abb.send(Stop())

    # Move robot to start position
    done = abb.send_and_wait(MoveToJoints(robot_joints_start_position, external_axis_dummy, 1000, Zone.FINE))

    # User message and input
    input('Robot start position reached, press any key to start the print.')

    # Move to print start
    abb.send(MoveToFrame(frame_print_start, 500, Zone.FINE))

    # Start watch
    done = abb.send_and_wait(StartWatch())

    # Start print
    abb.send(SetDigital('doPrintTX', 1))

    # Print path
    abb.send(MoveToFrame(frame_print_end, 150, Zone.FINE, Motion.LINEAR))

    # End print
    abb.send(SetDigital('doPrintTX', 0))

    # Stop watch
    done = abb.send_and_wait(StopWatch())

    # Read watch
    future = abb.send(ReadWatch())

    # Move robot to end position
    abb.send(MoveToJoints(robot_joints_end_position, external_axis_dummy, 1000, Zone.FINE))

    # Read and print printing time
    watch_time = future.result(timeout=3.0)
    print('Print Time [s] = ', watch_time)

    # Print Text
    done = abb.send_and_wait(PrintText('Compas_RRC Example finish.'))

    # End of Code
    print('Compas_RRC Example finish.')

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
