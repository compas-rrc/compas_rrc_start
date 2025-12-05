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

---

### Recommended Startup Procedure

Follow the steps below in the given order to ensure a smooth startup of the robot system:

#### 1. Preparation

- Stop the robot application.  
- Bring down Docker containers (`docker-compose down`).  
- Close all open terminal sessions.

#### 2. Start the Robot

- Do **PP-Main** and starte application on the **FlexPendant**.  
- On the FlexPendant display, verify the following status for each task:

  - `T_ROB1 → RRC Main`  
  - `T_CTRL → RRC Main`  
  - `T_RX → RRC Main`  
  - `T_TX → RRC Main`  

#### 3. Start Docker Containers

- Bring up the Docker environment (`docker-compose up`).  
- On the FlexPendant display, verify the following status for the controller task:
  - `T_CTRL → RRC Connected`

#### 4. Launch Python Code

- Run your Python script (e.g., `welcome.py`) from VS Code.
- Verify that the code executes and that the robot starts performing actions — in this case, a print output of `Welcome to COMPAS_RRC`.

#### NOTE: 
- As long as your code is error-free, you can launch scripts sequentially.  
- If errors occur or the system becomes unsynchronized, killing the terminal and **PP-Main** on the FlexPendant usually resolves the issue.  
- In some cases, it may be necessary to restart the procedure from **Step 1**.






