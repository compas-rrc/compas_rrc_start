# Work in progress

## Outline of the new version: 

- Explaination of Repo 
- Explaination of possible workflows 
- COMPAS_RRC Installation on the PC
- How to open the demo RobotStuio stations
- How to connect with Docker (only virtual robots)
- Run the examples
- Explain the cheat sheets (python instructions) with the hello world example 
- Link to COMPAS_RRC_ABB (incl. / link to license description _ABB repo)
- Link to Workshops
- Link to forum for help

### RobotStudio Stations 
- 3D Printing with IRB4600 (pure python)
- Pick and Place with IRB910 (pure python)
- 2D Drawing with CRB15000 (with Rhino/GH)

- MultiMove Demo (only viewer)

### Not included
- no robotstudio training -> go to ABB 
- no station creation with robotstudio -> go to ABB 
- no tool and work object creation -> go to COMPAS_RRC_ABB


### CustomInstruction 
- update to:

    - PYTHON:

    done = abb.send_and_wait(rrc.CustomInstruction('r_RRC_CustomInstruction', ['Text1','Text2'], [1.0,2.0]))

    - RAPID: 

        ! Placehoder for your Code     
        
        r_RRC_FAddString("Tex1");
        r_RRC_FAddString("Tex2");

        r_RRC_FAddValue(1.0);
        r_RRC_FAddValue(2.0);















