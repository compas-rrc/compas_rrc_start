import compas_rrc as rrc
from compas.geometry import Frame
from compas_fab.backends.ros import RosClient

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

    # Get and move to joints
    if on:

        # Get joints
        robot_joints, external_axes = abb.send_and_wait(GetJoints())

        # Print received values
        print(robot_joints, external_axes)

        # Change value and move to new position
        robot_joints.rax_1 += 15
        speed = 100 # Unit [mm/s]
        done = abb.send_and_wait(MoveToJoints(robot_joints, external_axes, speed, Zone.FINE))

    # Get and move to frame
    if off:

        # Get frame
        frame = abb.send_and_wait(GetFrame())

        # Print received values
        print(frame)

        # Change any frame value and move robot to new position
        frame.point[0] += 50
        speed = 100 # Unit [mm/s]
        done = abb.send_and_wait(MoveToFrame(frame, speed, Zone.FINE, Motion.LINEAR))

    # Get and move to robtarget
    if off:

        # Get frame and external axes 
        frame, external_axes = abb.send_and_wait(GetRobtarget())

        # Print received values
        print(frame, external_axes)

        # Change any value and move to new position
        frame.point[0] += 50
        speed = 100 # Unit [mm/s]
        done = abb.send_and_wait(MoveToRobtarget(frame, external_axes, speed, Zone.FINE))

    # Move robot to start position
    if off:

        # Set start values
        robot_joints, external_axes =[0.0, -30, 0, 0, 30, 0],  []

        # Move robot to start position
        done = abb.send_and_wait(MoveToJoints(robot_joints, external_axes, 1000, Zone.FINE))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()

