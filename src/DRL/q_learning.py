import itertools
import sys
from collections import defaultdict
from environment import env
import numpy as np
import datetime

def make_epsilon_greedy_policy(Q, epsilon, nA):
    def policy_fn(observation):
        print("observation: ", observation)
        A = np.ones(nA, dtype=float) * epsilon / nA
        best_action = np.argmax(Q[observation])
        A[best_action] += (1.0 - epsilon)
        return A
    return policy_fn

def q_learning(env, num_episodes, discount_factor=1.0, alpha=0.5, epsilon=0.1):    
    Q = defaultdict(lambda: np.zeros(env.action_space()))
    
    policy = make_epsilon_greedy_policy(Q, epsilon, env.action_space())
    
    for i_episode in range(num_episodes):
        # Print out which episode we're on, useful for debugging.
        if (i_episode + 1) % 100 == 0:
            print("\rEpisode {}/{}.".format(i_episode + 1, num_episodes))
            sys.stdout.flush()
        
        # Reset the environment and pick the first action
        state = env.reset()
        
        # One step in the environment
        for t in itertools.count():
            
            # Take a step
            action_probs = policy(state)
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state, reward, done = env.step(action)
            
            # TD Update
            best_next_action = np.argmax(Q[next_state])
            print("Decided Action: ", best_next_action)
            td_target = reward + discount_factor * Q[next_state][best_next_action]
            td_delta = td_target - Q[state][action]
            Q[state][action] += alpha * td_delta
                
            if done:
                break
                
            state = next_state
    return Q

def demo_q_learning(env, num_episodes, discount_factor=1.0, alpha=0.5, epsilon=0.1):    
    Q = defaultdict(lambda: np.zeros(env.action_space.n))
    policy = make_epsilon_greedy_policy(Q, epsilon, env.action_space.n)
    
    for i_episode in range(num_episodes):
        # Print out which episode we're on, useful for debugging.
        if (i_episode + 1) % 100 == 0:
            print("\rEpisode {}/{}.".format(i_episode + 1, num_episodes))
            sys.stdout.flush()
        
        # Reset the environment and pick the first action
        state = env.reset()
        
        # One step in the environment
        total_reward = 0.0
        for t in itertools.count():
            
            # Take a step
            action_probs = policy(state)
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state, reward, done, _ = env.step(action)
            
            # TD Update
            best_next_action = np.argmax(Q[next_state])
            print("Decided Action: ", best_next_action)
            td_target = reward + discount_factor * Q[next_state][best_next_action]
            td_delta = td_target - Q[state][action]
            Q[state][action] += alpha * td_delta
                
            if done:
                break
                
            state = next_state
    return Q

if __name__ == '__main__':
    if sys.argv[1] == "--h":
        print("USAGE: python q_learning.py --<demo or train>")
        print("--demo  => run the demo app using CliffWalkingEnv")
        print("--train => run the demo app using RL")
        sys.exit()
    elif sys.argv[1] == "--train":
        n_episode = 5000
        env = env(n_episode)
        print("0:", datetime.datetime.now())
        Q = q_learning(env, n_episode)
        print("Q value: ", Q)
    elif sys.argv[1] == "--demo":
        from cliff_walking import CliffWalkingEnv
        n_episode = 5000
        print("Demo Training RUN")
        env = CliffWalkingEnv()
        Q = demo_q_learning(env, n_episode)
        print("Q value: ", Q)