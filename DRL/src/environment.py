import numpy as np
from dist_sensor import get_distance

class env:
    def __init__(self, n_episode):
        self.n_episode = n_episode
        self.action = ['go_further_forward', 'go_forward', 'go_backward', 'go_further_backward']

    def _generator(self):
        val = get_distance(port="/dev/cu.wchusbserial14310")
        # return np.random.rand(self.n_episode).flatten()
        # return np.random.randint(100)
        return val

    def step(self, action):
        self._action(action)
        state = self._generator()
        reward = 1 if not state < 50 else -1
        done = True if not state < 50 else False
        return state, reward, done

    def _action(self, action):
        # TO-DO
        # send the action to the robot!
        pass

    def reset(self):
        state = self._generator()
        return state

    def observation_space(self):
        return False

    def action_space(self):
        return len(self.action)

if __name__ == '__main__':
    n_episode = 4
    env = env(n_episode)
    # print(env.step())
    # print(env.action_space())
    for i in range(100):
        print(env._generator())