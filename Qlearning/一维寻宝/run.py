"""
Reinforcement learning  example.
"""

from RL_brain import QLearningTable,Environment
import time

def update():
    print('开始寻宝!')
    for episode in range(10):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            time.sleep(0.2)

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(observation, observation_,action, reward)

            # swap observation
            observation = observation_
            env.render()

            # break while loop when end of this episode
            if done:
                print('这回合花了%d步'%env.steps)
                break

    # end of game
    print('game over')

if __name__ == "__main__":
    env = Environment()
    RL = QLearningTable()
    update()
    print(RL.Qtable)