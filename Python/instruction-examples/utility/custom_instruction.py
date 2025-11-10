import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # ========================================================================================================================
    # Call of CustomInstruction
    # ========================================================================================================================
    #
    # 'r_RRC_CustomInstruction': Name of the RAPID procedure to be called.
    #                            'r_' is the recommended prefix for routines, and '_RRC_' 
    #                            is the reserved key for official RRC commands/functions in RAPID.
    #                            For your own custom instructions, use your own key such as '_ABC_' 
    #                            (3–4 characters recommended).
    #
    # ['Text1','Text2']:         Example showing how to pass up to 8 strings (each up to 80 characters) from Python to RAPID.
    #
    # [1.1,2.2]:                 Example showing how to pass up to 36 numeric values from Python to RAPID.
    #
    # ========================================================================================================================

    raw_debug_output = abb.send_and_wait(rrc.Debug(rrc.CustomInstruction('r_RRC_CustomInstruction', ['Python value 1: ','Python value 2: '], [1.11,2.22])))

    rapid_string_1 = raw_debug_output['string_values'][0]
    rapid_string_2 = raw_debug_output['string_values'][1]

    rapid_value_1 = round(raw_debug_output['float_values'][0],2)
    rapid_value_2 = round(raw_debug_output['float_values'][1],2)

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
