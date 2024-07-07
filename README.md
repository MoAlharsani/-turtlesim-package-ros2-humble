# turtlesim-package-ros2-humble
In this repo, I will build different controller for the Turtlesim package in the ROS2 Humble distro. These controllers hopefully will help learning and understanding ROS2 Concepts. 

### To-Do

- [ ] Make the turtle draw a shape where the shape is given by a set of points. ${\{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\}}$


### Completed

- [x] Make the turtle navigate to a given (x,y) point.
  - Implemented at the `GoToCoordinate` class



## GoToCoordinate.py 
is a node that make the turtle goes to a specifc point in turtuel 2D plane,

first install the package in your system, then following this commands
- Create workspace
  ```
  mkdir -p ~/artist_turtle_ros2_ws/src
  cd ~/artist_turtle_ros2_ws/src
  ros2 pkg create artist_turtle_controller --build-type ament_python --dependencies rclpy math sys geometry_msg 
  cd artist_turtle_controller/artist_turtle_controller/
  curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/go-to-coordinate/go_to_coordinate.py
  rm -rf setup.py
  curl -O https://raw.githubusercontent.com/MoAlharsani/turtlesim-package-ros2-humble/main/go-to-coordinate/setup.py
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
  
