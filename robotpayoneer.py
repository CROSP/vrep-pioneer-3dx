class RobotPayoneer(object):
    SIMULATION_TIME_SIGNAL = "CurrentSimulationTimeSignal"
    OPMODE_BLOCKING = ""
    OPMODE_STREAMING = ""
    ROBOT_LEFT_MOTOR = "leftMotor"
    ROBOT_RIGHT_MOTOR = "rightMotor"

    def __init__(self, vrep_handler, client_id, robot_name="Pioneer_p3dx"):
        self.vrep_hndlr = vrep_handler
        self.obstacles = {}
        self.robot_name = robot_name
        self.client_id = client_id
        RobotPayoneer.OPMODE_BLOCKING = self.vrep_hndlr.simx_opmode_oneshot_wait
        RobotPayoneer.OPMODE_STREAMING = self.vrep_hndlr.simx_opmode_streaming
        self.robot_handler = self.get_object_handler(self.robot_name)
        self.robot_left_motor = self.get_object_handler(self.robot_name + "_" + RobotPayoneer.ROBOT_LEFT_MOTOR)
        self.robot_right_motor = self.get_object_handler(self.robot_name + "_" + RobotPayoneer.ROBOT_RIGHT_MOTOR)

    def find_all_shapes(self, shape_numbers, shape_prefix="shape_"):
        for shape_num in shape_numbers:
            shape_name = shape_prefix + str(shape_num)
            self.obstacles[shape_name] = self.get_object_handler(shape_name)

    def get_object_handler(self, object_name):
        error, handler = self.vrep_hndlr.simxGetObjectHandle(self.client_id, object_name,
                                                             RobotPayoneer.OPMODE_BLOCKING)
        return handler

    def get_current_simulation_time(self):
        code, sim_time = self.vrep_hndlr.simxGetFloatSignal(self.client_id, RobotPayoneer.SIMULATION_TIME_SIGNAL,
                                                            RobotPayoneer.OPMODE_BLOCKING)
        return sim_time

    def wait_until(self, sim_time_until):
        current_sim_time = self.get_current_simulation_time()
        while current_sim_time < sim_time_until:
            current_sim_time = self.get_current_simulation_time()

    def wait_for(self, sim_time):
        # Fist time it returns 0, why ?
        initial_sim_time = self.get_current_simulation_time()
        initial_sim_time = self.get_current_simulation_time()
        current_sim_time = self.get_current_simulation_time()
        while current_sim_time - initial_sim_time < sim_time:
            current_sim_time = self.get_current_simulation_time()

    def set_motors_velocity(self, left_velocity, right_velocity):
        self.set_robot_motor_velocity(RobotPayoneer.ROBOT_LEFT_MOTOR, left_velocity)
        self.set_robot_motor_velocity(RobotPayoneer.ROBOT_RIGHT_MOTOR, right_velocity)

    def set_robot_motor_velocity(self, motor, velocity):
        if motor == RobotPayoneer.ROBOT_RIGHT_MOTOR:
            errorCode = self.vrep_hndlr.simxSetJointTargetVelocity(self.client_id, self.robot_right_motor, velocity,
                                                                   RobotPayoneer.OPMODE_BLOCKING)
        elif motor == RobotPayoneer.ROBOT_LEFT_MOTOR:
            errorCode = self.vrep_hndlr.simxSetJointTargetVelocity(self.client_id, self.robot_left_motor, velocity,
                                                                   RobotPayoneer.OPMODE_BLOCKING)

    def stop_robot(self):
        self.set_robot_motor_velocity(RobotPayoneer.ROBOT_LEFT_MOTOR, 0)
        self.set_robot_motor_velocity(RobotPayoneer.ROBOT_RIGHT_MOTOR, 0)

    def get_self_position(self):
        errors, position = self.vrep_hndlr.simxGetObjectPosition(self.client_id, self.robot_handler, -1,
                                                                 RobotPayoneer.OPMODE_BLOCKING)
        return position

    def get_object_position(self, object_name):
        object_handler = self.get_object_handler(object_name)
        errors, position = self.vrep_hndlr.simxGetObjectPosition(self.client_id, object_handler, -1,
                                                                 RobotPayoneer.OPMODE_BLOCKING)
        return position

    def start_simulation(self):
        self.vrep_hndlr.simxStartSimulation(self.client_id, RobotPayoneer.OPMODE_BLOCKING)

    def stop_simulation(self):
        self.vrep_hndlr.simxStopSimulation(self.client_id, RobotPayoneer.OPMODE_BLOCKING)

    def get_obstacle_object_position(self, object_name):
        if object_name in self.obstacles:
            object_handler = self.obstacles[object_name]
            errors, position = self.vrep_hndlr.simxGetObjectPosition(self.client_id, object_handler, -1,
                                                                     RobotPayoneer.OPMODE_BLOCKING)
            return position
        else:
            print("No such obstacle is defined")
