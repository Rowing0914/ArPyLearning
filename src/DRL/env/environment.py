import numpy as np
from distance_sensor import Sensor
from control_agent import Robot
import datetime
from pyfirmata import Arduino, util
import time

class env:
    def __init__(self, n_episode):
        self.board = Arduino('/dev/cu.usbmodem14111')
        self.sensor = Sensor(self.board, pin=1)
        self.robot = Robot(self.board)
        self.n_episode = n_episode
        # self.action = ['go_further_forward', 'go_forward', 'go_backward', 'go_further_backward']
        self.action = ['go_forward', 'go_backward']

    def _generator(self):
        print("state: " ,self.sensor.get_distance())
        return self.sensor.get_distance()
        # return np.random.rand(self.n_episode).flatten()
        # return np.random.randint(100)

    def step(self, action):
        print("2: ", datetime.datetime.now())
        self._action(action)
        print("3: ", datetime.datetime.now())
        print("action: ", action)
        state = self._generator()
        print("4: ", datetime.datetime.now())
        reward = 1 if not state < 0.2 else -1
        done = True if not state < 0.2 else False
        return state, reward, done

    def _action(self, action):
        # send the action to the robot!
        if action == 0:
            self.robot.move_backward()
        elif action == 1:
            self.robot.move_forward()
        elif action == 2:
            self.robot.stop()
        pass

    def reset(self):
        print("1: ", datetime.datetime.now())
        state = self._generator()
        return state

    def observation_space(self):
        return False

    def action_space(self):
        return len(self.action)

if __name__ == '__main__':
    n_episode = 4
    env = env(n_episode)
    # print(env.action_space())
    while True:
        print(env._generator())
        print(env.step(1))


