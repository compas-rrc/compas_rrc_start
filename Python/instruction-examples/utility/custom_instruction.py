import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # =========================================================================================================
    # EXAMPLE: CustomInstruction
    # =========================================================================================================
    #
    # The CustomInstruction allows you to call a RAPID procedure with custom arguments.
    #
    # 'r_RRC_CustomInstruction':
    #     - Name of the RAPID procedure to be executed on the robot controller.
    #     - By convention, use 'r_' as prefix for routines.
    #     - '_RRC_' is reserved for official RRC functions; for your own routines, use a unique key, e.g. '_ABC_' (3–4 characters recommended).
    #
    # ['Python value 1: ','Python value 2: ']:
    #     - Example string arguments passed from Python to RAPID.
    #     - Up to 8 strings can be sent, each with max. 80 characters.
    #
    # [1.11,2.22]:
    #     - Example float arguments passed from Python to RAPID.
    #     - Up to 36 numeric values can be provided.
    #
    # The RAPID routine processes the input and sends custom output data
    # (up to 8 strings and 36 floats) back to Python as feedback.
    # =========================================================================================================

    # Syntax:
    custominstruction_feedback = abb.send_and_wait(rrc.Debug(rrc.CustomInstruction('r_RRC_CustomInstruction', ['Python value 1: ','Python value 2: '], [1.11,2.22])))

    # Read custom insturction string feedback 
    rapid_string_1 = custominstruction_feedback['string_values'][0]
    rapid_string_2 = custominstruction_feedback['string_values'][1]

    # Read custom insturction float feedback rounded to 2 decimals
    rapid_value_1 = round(custominstruction_feedback['float_values'][0],2)
    rapid_value_2 = round(custominstruction_feedback['float_values'][1],2)

    # Print feedback from RAPID:
    print(rapid_string_1, rapid_value_1)
    print(rapid_string_2, rapid_value_2)

    # End of CustomInstruction example
    # ========================================================================================================================

    # No operation 
    done = abb.send_and_wait(rrc.Noop())

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
