import numpy as np
import serial
import time
from Arduino import Arduino
from DRL.src.DQN import DQNAgent

def demo(board, pin_servo):
	board.Servos.attach(pin_servo) #declare servo on pin pin_servo
	board.Servos.write(pin_servo, 180) #move servo on pin pin_servo to 0 degrees
	print board.Servos.read(pin_servo) # should be 0
	time.sleep(0.5)
	board.Servos.detach(pin_servo) #free pin pin_servo
	return 'done'

def action_degree(action):
	if action == 0:
		degree = np.random.randint(0, 90)
	else:
		degree = np.random.randint(90, 180)
	return degree

def control_servo(board, pin_servo, action):
	degree = action_degree(action)
	board.Servos.attach(pin_servo) # declare servo on pin pin_servo
	board.Servos.write(pin_servo, 180) # move servo on pin pin_servo to 0 degrees
	print board.Servos.read(pin_servo) # should be 0
	time.sleep(0.5)
	board.Servos.detach(pin_servo) #free pin pin_servo
	return 'done'	

if __name__ == '__main__':
	pin_servo = 9
	board = Arduino('9600', port='/dev/cu.usbmodem14311')
	# demo(board, pin_servo)

	env = gym.make('CartPole-v1')
	state_size = env.observation_space.shape[0]
	action_size = env.action_space.n
	agent = DQNAgent(state_size, action_size)
	agent.load("./DRL/models/cartpole-dqn.h5")
	done = False
	batch_size = 32

	for e in range(EPISODES):
		state = env.reset()
		state = np.reshape(state, [1, state_size])
		for time in range(500):
			# env.render()
			action = agent.act(state)
			next_state, reward, done, _ = env.step(action)
			control_servo(board, pin_servo, action)
			reward = reward if not done else -10
			next_state = np.reshape(next_state, [1, state_size])
			agent.remember(state, action, reward, next_state, done)
			state = next_state
			if done:
				print("episode: {}/{}, score: {}, e: {:.2}"
					  .format(e, EPISODES, time, agent.epsilon))
				break
			if len(agent.memory) > batch_size:
				agent.replay(batch_size)

	# agent.save("cartpole-dqn.h5")

	for e in range(EPISODES):
		state = env.reset()
		env.render()
		state = np.reshape(state, [1, state_size])
		for time in range(500):
			action = agent.act(state)
			next_state, reward, done, _ = env.step(action)
			reward = reward if not done else -10
			next_state = np.reshape(next_state, [1, state_size])
			state = next_state
			if done:
				break