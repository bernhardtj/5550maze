# Group 2 Maze Code
## Instructions for use (on EC2 machine):
1. Clone this repository. `git clone https://github.com/bernhardtj/5550maze`
2. Run a program: `cd 5550maze; bash slam.sh`

For each problem, make a script that sources `setup.sh` and runs a launch file.
Add to `setup.sh` as needed.
Python nodes can be included with a snippet in `setup.sh` like the translator.

## Problem Definition
There are two Turtlebot3 Burger robots in this problem.
Robot M is the master robot. Robot S is the slave robot. They can only communicate on a topic called `/comm` which is of type `std_msgs/String`.

Burger robots have a laser scanner for SLAM.
