# Getting started with COMPAS RRC

 > COMPAS RRC is a robot driver for ABB robots based on COMPAS/COMPAS_FAB

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) Docker Toolbox would also work but it's a bit more annoying. After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Quickstart

### Setup robot station

* Unpack a `Pack&Go` file using ABB RobotStudio
* Open flexpendant
* Start the simulation

### Start ROS driver

* Make sure Docker Desktop is running
* Compose up the `docker-compose.yml` file in the `docker` folder

### Run examples

* Make sure your conda environment has `compas_rrc` installed.
* Go to the `python` folder
* Run `compas_rrc_A_welcome.py`
