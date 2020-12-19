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

# Package: frontier explorer
cd "$WS/src" && git clone https://github.com/hrnr/m-explore

# Package: obstacle detector
cd "$WS/src" && git clone https://github.com/tysik/obstacle_detector

# Package: user code (main)
cd "$WS/src" && catkin_create_pkg main rospy
source "$WS/devel/setup.bash" && roscd main
for script in $SRCDIR/scripts/*.py; do
    install -Dvm755 "$script" "scripts/$(basename $script)"
done
for launch in $SRCDIR/launch/*.launch.xml; do
    install -Dvm755 "$launch" "launch/$(basename ${launch%.*})"
done
for config in $SRCDIR/config/*; do
    install -Dvm755 "$launch" "config/$(basename ${config%.*})"
done
cat <<EOF >>CMakeLists.txt
catkin_install_python(PROGRAMS $(find scripts -name "*.py" -exec printf "{} " \;)
  DESTINATION \${CATKIN_PACKAGE_BIN_DESTINATION}
)
EOF

# Build project
cd "$WS" && catkin_make

# ----- TASK 1 ----- #
# export TURTLEBOT3_MODEL=burger
# source "$WS/devel/setup.bash" && roslaunch main slam.launch

# ----- TASK 2 ----- #
# export TURTLEBOT3_MODEL=burger
# source "$WS/devel/setup.bash" && roslaunch main goal_listener.launch

# ----- TASK 3 ----- #
# export TURTLEBOT3_MODEL=burger
# source "$WS/devel/setup.bash" && roslaunch main robots.launch
