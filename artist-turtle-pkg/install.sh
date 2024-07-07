#!/bin/bash


# Create ROS 2 workspace and navigate to src directory
mkdir -p ~/artist_turtle_ros2_ws/src
cd ~/artist_turtle_ros2_ws/src

# Create ROS 2 package 'artist_turtle_controller'
ros2 pkg create artist_turtle_controller --build-type ament_python --dependencies rclpy math sys geometry_msgs

# Navigate into the package directory
cd artist_turtle_controller

# Remove existing setup.py and download new one
rm -f setup.py
curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/artist-turtle-pkg/setup.py

# Download go_to_coordinate.py and make it executable
curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/artist-turtle-pkg/go_to_coordinate.py
chmod +x go_to_coordinate.py

# Navigate back to the workspace root and build the workspace
cd ~/artist_turtle_ros2_ws
colcon build

echo "Installation and build complete."
