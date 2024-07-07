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
  mkdir -p ~/ros2_ws/src
  cd ~/ros2_ws/src
  ```
- Clone the packege into your src file
  ```
  # Clone the repository with depth 1 to get only the latest commit
  git clone --depth 1 https://github.com/MoAlharsani/turtlesim-package-ros2-humble.git
  
  # Move the contents of the 'artist_turtle_controller' directory to your current directory
  mv turtlesim-package-ros2-humble/artist_turtle_controller/* .
  
  # Clean up: Remove the temporary directory
  rm -rf turtlesim-package-ros2-humble
  ```
- Build the workspace
  ```
  cd ~/ros2_ws
  colcon build
  ```
- In another terminal run the turtlesim_node
  ```
  ros2 run turtlesim turtlesim_node
  ```
- In another terminal, source and run the package. Where $(x, y) = (1.0, 7.0)$
  ```
  source ~/ros2_ws/install/setup.sh
  ros2 run artist_turtle_controller go_to_coordinate 1.0 7.0 
  ```
  
