# artist-turtle-pkg-ros2-humble
This repository provides controllers for the Turtlesim package in ROS 2 Humble. These controllers enable the turtle to perform tasks such as navigating to specific points and drawing predefined shapes on the 2D plane, serving as practical examples for learning ROS 2 concepts and robotics programming.

### To-Do

- [ ] Make the turtle draw a shape where the shape is given by a set of points. ${\{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\}}$
- [ ] Installing the package using Docker Containers



### Completed

- [x] Make the turtle navigate to a given (x,y) point.
  - Implemented at the `GoToCoordinate` class
- [x] Write the shell installation process



## Package Installation
Here is how to install the package


### Step By Step Installation

- Create workspace
  ```
  mkdir -p ~/artist_turtle_ros2_ws/src
  cd ~/artist_turtle_ros2_ws/src
  ros2 pkg create artist_turtle_controller --build-type ament_python --dependencies rclpy math sys geometry_msg 
  cd artist_turtle_controller/
  rm -rf setup.py
  curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/artist-turtle-pkg/setup.py
  cd artist_turtle_controller/
  curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/artist-turtle-pkg/go_to_coordinate.py
  chmod +x go_to_coordinate.py
  ```
- Build the workspace
  ```
  cd ~/artist_turtle_ros2_ws
  colcon build
  ```
- In another terminal run the turtlesim_node
  ```
  ros2 run turtlesim turtlesim_node
  ```
- In another terminal, source and run the package. Where $(x, y) = (1.0, 7.0)$
  ```
  source ~/artist_turtle_ros2_ws/install/setup.sh
  ros2 run artist_turtle_controller go_to_coordinate 1.0 7.0 
  ```

![gif-ezgif com-video-to-gif-converter](https://github.com/MoAlharsani/turtlesim-package-ros2-humble/assets/86081496/be54b9cc-352a-4b72-b185-5bd64929c1ec)

### Docker Container installation 
- In the Future

