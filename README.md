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
- 

