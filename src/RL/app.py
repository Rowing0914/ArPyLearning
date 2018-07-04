import numpy as np
import serial
import time
from ArPyLearning.Arduino import Arduino
from RL.DQN import DQNAgent, env_init

def demo_(board, pin_servo):
	board.Servos.attach(pin_servo) #declare servo on pin pin_servo
	board.Servos.write(pin_servo, 180) #move servo on pin pin_servo to 0 degrees
	print(board.Servos.read(pin_servo)) # should be 0
	time.sleep(0.5)
	board.Servos.detach(pin_servo) #free pin pin_servo
	return 'done'

def action_degree(action):
	if action == 0:
		# degree = 30
		degree = np.random.randint(0, 90)
	else:
		# degree = 100
		degree = np.random.randint(90, 180)
	print(degree)
	return degree

def control_servo(board, pin_servo, action):
	degree = action_degree(action)
	board.Servos.attach(pin_servo) # declare servo on pin pin_servo
	board.Servos.write(pin_servo, degree) # move servo on pin pin_servo to 0 degrees
	print(board.Servos.read(pin_servo)) # should be 0
	time.sleep(0.5)
	board.Servos.detach(pin_servo) #free pin pin_servo
	return 'done'	

def demo(agent, env, EPISODES, state_size, batch_size):
	done = False
	for e in range(EPISODES):
		state = env.reset()
		env.render()
		state = np.reshape(state, [1, state_size])
		for episode in range(500):
			action = agent.act(state)
			next_state, reward, done, _ = env.step(action)
			control_servo(board, pin_servo, action)
			reward = reward if not done else -10
			next_state = np.reshape(next_state, [1, state_size])
			state = next_state
			if done:
				break

# def q_learning():

if __name__ == '__main__':
	EPISODES = 50
	pin_servo = 9
	batch_size = 32
	game_name = 'CartPole-v1'

	board = Arduino('9600', port='/dev/cu.usbmodem14311')
	# demo_(board, pin_servo)

	# initialise game
	env, state_size, action_size = env_init(game_name)

	# initialise agent
	agent = DQNAgent(state_size, action_size)

	# load model
	agent.load("../models/cartpole-dqn.h5")

	# train
	# agent.train(agent, env, EPISODES, state_size, batch_size)

	# save model/agent state
	agent.save("cartpole-dqn.h5")

	# move servo!!
	demo(agent, env, EPISODES, state_size, batch_size)