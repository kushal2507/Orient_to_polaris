# Orient_to_polaris

* Usage
  
  After setting up your environment, from catkin_ws folder source the bash file and in two separate terminals carry out the following commands: 
  
  roslaunch turtlebot_sim simulation.launch
  
  roslaunch orient_to_polaris solution.launch
  
* Functionality

  Turtlebot loads itself to default position of 0,0,0 (Can be changed in simulation.launch file) and twists along yaw to orient itself to a pre-defined direction of Polaris using a simple proportional controller.
  
  In case one needs to change the orientation of the bot, in a separate terminal carry out the following commands:
  
  rosrun turtle_teleop_keyboard turtle_teleop_keyboard.py
   
