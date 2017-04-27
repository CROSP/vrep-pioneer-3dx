import sys

import vrep
from robotpayoneer import RobotPayoneer

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 66666, True, True, 5000, 5)

if clientID != -1:
    print("Connected to a remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

robot_handler = RobotPayoneer(vrep, clientID)
robot_handler.find_all_shapes((1, 2, 3, 4, 5, 6, 7, 8), "sphere_")
robot_handler.start_simulation()
start_time = robot_handler.get_current_simulation_time()
# First sphere
# Turn right
robot_handler.set_motors_velocity(5, 2.5)
robot_handler.wait_for(1.5)
# Turn left
robot_handler.set_motors_velocity(3.5, 3)
robot_handler.wait_for(3)
# Second Sphere
# Go around second sphere from left side
robot_handler.set_motors_velocity(3, 5)
robot_handler.wait_for(4)
robot_handler.set_motors_velocity(5, 4)
robot_handler.wait_for(3)
# Turn right
robot_handler.set_motors_velocity(6, 5)
robot_handler.wait_for(3)
robot_handler.set_motors_velocity(7, 7)
robot_handler.wait_for(1)
robot_handler.set_motors_velocity(5, 8)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(7, 6)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(7, 4)
robot_handler.wait_for(4)
robot_handler.set_motors_velocity(7, 5)
robot_handler.wait_for(3)
robot_handler.set_motors_velocity(6, 7)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(9, 5)
robot_handler.wait_for(5)
robot_handler.set_motors_velocity(6, 7)
robot_handler.wait_for(3)
robot_handler.set_motors_velocity(5, 7)
robot_handler.wait_for(3)
robot_handler.set_motors_velocity(10, 7)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(6, 4)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(8, 10)
robot_handler.wait_for(2)
robot_handler.set_motors_velocity(7, 8)
robot_handler.wait_for(4)
# Go in diagonal direction


final_time = robot_handler.get_current_simulation_time() - start_time
print "TIME ELAPSED : " + str(final_time)
robot_handler.stop_simulation()
