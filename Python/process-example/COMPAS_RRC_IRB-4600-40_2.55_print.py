import compas_rrc as rrc
from compas.geometry import Frame 
from compas.geometry import Point
from compas.geometry import Vector

# ==============================================================
# Define joint robot positions (joint space, safe configurations)
# ==============================================================

PROCESS_START = [0.0, -20.0, 40.0, 0.0, -20.0, 0.0]
PROCESS_END = [0.0, -30.0, 50.0, 0.0, -20.0, 0.0]

# ==============================================================
# Define safe external axis positions (joint space)
# ==============================================================

# Only a placeholder no external axis is used in this example
EXT_AXIS = []

# ==============================================================
# Define process parameters (red print = x)
# ==============================================================

# Tool
TOOL_RED_X = 't_RRC_Tool_X'

# Frames
PRINT_RED_START_X = Frame(Point(750.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
PRINT_RED_END_X = Frame(Point(250.000, 250.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

# Print speed [mm/s]
PRINT_RED_SPEED_X = 50 

# Signal
SIGNAL_RED_X = 'do_X'

# ==============================================================
# Define process parameters (green print = y)
# ==============================================================

# Tool
TOOL_GREEN_Y = 't_RRC_Tool_Y'

# Frames
PRINT_GREEN_START_Y = Frame(Point(750.000, 350.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
PRINT_GREEN_END_Y = Frame(Point(250.000, 350.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

# Print speed [mm/s]
PRINT_GREEN_SPEED_Y = 100

# Signal
SIGNAL_GREEN_Y = 'do_Y'

# ==============================================================
# Define process parameters (blue print = z)
# ==============================================================

# Tool
TOOL_BLUE_Z = 't_RRC_Tool_Z'

# Frames
PRINT_BLUE_START_Z = Frame(Point(750.000, 450.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))
PRINT_BLUE_END_Z = Frame(Point(250.000, 450.000, -0.000), Vector(-1.000, 0.000, 0.000), Vector(0.000, 1.000, 0.000))

# Print speed [mm/s]
PRINT_BLUE_SPEED_Z = 150

# Signal
SIGNAL_BLUE_Z = 'do_Z'

# ==============================================================
# General process parameters 
# ==============================================================

# Define speeds 
SPEED = 300

# Define acceleration settings
ACCELERATION = 100  # Unit [%]
ACCELERATION_RAMP = 100  # Unit [%]

# Define override and max speed
OVERRIDE = 100  # Unit [%]
MAX_TCP = 1000  # Unit [mm/s]

# Define work object reference cordination system for frames
WORKPLACE = 'ob_RRC_Workplace'

# ==============================================================
# Option to demonstrate the user interaction on terminal and flexpendant
# ==============================================================

USER_INTERACTION = False
# (Make sure to open the FlexPendant in RobotStudio before you start the simulation)

# ==============================================================
# Process logic 
# ==============================================================

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Reset signals 
    abb.send(rrc.SetDigital(SIGNAL_RED_X,0))
    abb.send(rrc.SetDigital(SIGNAL_GREEN_Y,0)) 
    abb.send(rrc.SetDigital(SIGNAL_BLUE_Z,0))

    # Set acceleration and max speed
    abb.send(rrc.SetAcceleration(ACCELERATION, ACCELERATION_RAMP))
    abb.send(rrc.SetMaxSpeed(OVERRIDE, MAX_TCP))

    # Set work object
    abb.send(rrc.SetWorkObject(WORKPLACE))

    # User message -> basic settings send to robot
    print('Work Object, Acceleration and Speed limits sent to robot')
    print(' ')

    # User interaction FlexPendant
    if USER_INTERACTION:

        # Stop task user must press play button on the FlexPendant (RobotStudio) before robot starts to move
        abb.send(rrc.PrintText('Press Play to move.'))
        abb.send(rrc.Stop())

    # Move robot to start position
    done = abb.send_and_wait(rrc.MoveToJoints(PROCESS_START, EXT_AXIS, SPEED, rrc.Zone.FINE))

    # User interaction terminal
    if USER_INTERACTION:

        # User message and input
        input('Robot start position reached, press any key to start the print.')

    # Loop variables
    cycle = 0
    printing = True

    # Printing  loop for all three colors
    while printing: 

        # Increase cycle counter
        cycle += 1

        # 
        match cycle:

            case 1:

                # Red print (x)
                print_tool = TOOL_RED_X
                print_start = PRINT_RED_START_X
                print_end = PRINT_RED_END_X
                print_speed = PRINT_RED_SPEED_X
                print_signal = SIGNAL_RED_X
        
            case 2:

                # Green print (y)
                print_tool = TOOL_GREEN_Y
                print_start = PRINT_GREEN_START_Y
                print_end = PRINT_GREEN_END_Y
                print_speed = PRINT_GREEN_SPEED_Y
                print_signal = SIGNAL_GREEN_Y
        
            case 3:

                # Blue print (z)
                print_tool = TOOL_BLUE_Z
                print_start = PRINT_BLUE_START_Z
                print_end = PRINT_BLUE_END_Z
                print_speed = PRINT_BLUE_SPEED_Z
                print_signal = SIGNAL_BLUE_Z
            

        # Set tool current print tool 
        abb.send(rrc.SetTool(print_tool))

        # User message -> basic settings send to robot
        print('Tool updated to {}'.format(print_tool))

        # Move to print start
        abb.send(rrc.MoveToFrame(print_start, SPEED, rrc.Zone.FINE))

        # Start watch
        done = abb.send(rrc.StartWatch())

        # Start print
        abb.send(rrc.SetDigital(print_signal, 1))

        # Move to print end
        abb.send(rrc.MoveToFrame(print_end, print_speed, rrc.Zone.FINE, rrc.Motion.LINEAR))

        # End print
        abb.send(rrc.SetDigital(print_signal, 0))

        # Stop watch
        done = abb.send_and_wait(rrc.StopWatch())

        # Read watch
        future = abb.send(rrc.ReadWatch())

        # Move robot to end position
        abb.send(rrc.MoveToJoints(PROCESS_END, EXT_AXIS, SPEED, rrc.Zone.FINE))

        # Read and print printing time
        watch_time = future.result(timeout=3.0)
        print('Print ({}) Time [s] = '.format(cycle), watch_time)
        print(' ')

        # Check for end of printing 
        if cycle == 3:
            
            # End printing loop 
            printing = False
    
    # Print Text
    done = abb.send_and_wait(rrc.PrintText('Compas_RRC Example finish.'))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
