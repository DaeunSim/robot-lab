import matplotlib.pyplot as plt

# --- 1. PID controller ---
class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint # target point
        self.integral = 0.0      # sum of errors over time (I)
        self.last_error = 0.0    # The error from the previous time step (D)
        self.dt = 0.1            # time diff

    def compute(self, current_value): # current angle
        error = self.setpoint - current_value
        
        # P (Proportional)
        p_term = self.Kp * error
        
        # I (Integral)
        self.integral += error * self.dt
        i_term = self.Ki * self.integral
        
        # D (Derivative)
        derivative = (error - self.last_error) / self.dt
        d_term = self.Kd * derivative
        self.last_error = error
        
        # Total output
        return p_term + i_term + d_term
    
# --- 2. Physics ---
class VirtualGimbal:
    def __init__(self, initial_angle):
        self.angle = initial_angle
        self.dt = 0.1

    def update_physics(self, control_output):
        self.angle += control_output * self.dt
        self.angle *= 0.98 

    def get_sensor_value(self):
        import random
        noise = random.uniform(-0.5, 0.5) # -0.5 ~ +0.5 noise
        return self.angle + noise

# --- 3. Simulate gimbal ---
if __name__ == "__main__": 
    controller = PID(Kp=3.0, Ki=0.01, Kd=0.1, setpoint=0.0)
    gimbal = VirtualGimbal(initial_angle=50.0)

    angles_list = []
    setpoint_list = []

    print("simulation start...")
    for _ in range(300):
        current_angle_from_sensor = gimbal.get_sensor_value()
        control_output = controller.compute(current_angle_from_sensor)
        gimbal.update_physics(control_output)
        
        angles_list.append(gimbal.angle)
        setpoint_list.append(controller.setpoint)

    print("simulation finished...")

# --- 4. Visualization (matplotlib) ---
    plt.figure(figsize=(10, 6))
    plt.plot(angles_list, label='Gimbal Angle (Actual)')
    plt.plot(setpoint_list, label='Setpoint (Target)', linestyle='--', color='red')
    plt.title(f'PID Control Simulation (Kp={controller.Kp}, Ki={controller.Ki}, Kd={controller.Kd})')
    plt.xlabel('Time Steps')
    plt.ylabel('Angle (degrees)')
    plt.legend()
    plt.grid(True)
    plt.show()
