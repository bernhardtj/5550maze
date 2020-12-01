#!/bin/bash
export DISPLAY=:1

SRCDIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
WS=$SRCDIR/ws

# Ensure dependencies are installed
sudo apt-get install -y \
    ros-melodic-turtlebot3 \
    ros-melodic-slam-gmapping \
    ros-melodic-dwa-local-planner

# Initialize workspace
rm -rf "$WS"
source /opt/ros/melodic/setup.bash
mkdir -p "$WS/src" && cd "$WS" && catkin_make
source "$WS/devel/setup.bash"

# Package: virtual joystick
cd "$WS/src" && git clone https://github.com/aquahika/rqt_virtual_joystick

# Package: fira maze
cd "$WS/src" && git clone https://github.com/arixrobotics/fira_maze

# Package: reduced mesh robots for faster simulation (from the instructions)
cd "$WS/src" && git clone https://github.com/aws-robotics/turtlebot3-description-reduced-mesh

# Package: translator for virtual joystick
cd "$WS/src" && catkin_create_pkg translator rospy
source "$WS/devel/setup.bash" && roscd translator
install -Dvm755 "$SRCDIR/translator.py" scripts/translator.py
cat <<'EOF' >>CMakeLists.txt
catkin_install_python(PROGRAMS scripts/translator.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
EOF

# Package: general stuff (main)
cd "$WS/src" && catkin_create_pkg main rospy
source "$WS/devel/setup.bash" && roscd main
install -Dvm755 "$SRCDIR/slam.xml" launch/slam.launch

# Build project
cd "$WS" && catkin_make

