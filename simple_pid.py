import time

class Controller:
    def __init__(self, Kp: float, Ki: float, Kd: float, setpoint: float):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint
        self.last_time: float = time.time()
        self.last_error = 0
        self.error_sum = 0

    def update(self, input: float) -> float:
        time_now: float = time.time()
        error: float = self.setpoint - input
        print(f'setpoint is {self.setpoint} and input is {input}, so error is {error}')
        dt: int = time_now - self.last_time
        # For the integral bit
        self.error_sum += (error * dt)
        error_derivative: float = (error - self.last_error) / dt
        print(f'de/dt: {error_derivative}')
        # While we're here...
        self.last_time = time_now
        self.last_error = error
        # Kp*e(t) + Ki*int[e(t)] + Kd*(d[e(t)]/dt)
        return (self.Kp * error) + (self.Ki * self.error_sum) + (self.Kd * error_derivative)



