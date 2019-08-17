"""
Reinforcement learning  example.
"""

from RL_brain import QLearningTable,Environment
import time

def update(times=800,test=False):#test=False的时候用于训练，test=True的时候用于展览
    print('开始寻宝!')
    if test:
        times=1
    for episode in range(times):
        # initial observation
        observation = env.reset()
        #env.render()

        while True:
            # fresh env
            if test:
                time.sleep(0.5)

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            RL.check_exist(observation_)
            

            # RL learn from this transition
            RL.learn(observation, observation_,action, reward)

            # swap observation
            observation = observation_
            if test:
                env.render()

            # break while loop when end of this episode
            if done:
                print('这回合花了%d步'%env.steps)
                break

    # end of game
    if test:
        print('展示结束')
    else:
        print('game over,总共训练了%d次'%times)

if __name__ == "__main__":
    env = Environment()
    RL = QLearningTable()
    update(times=400)#这个数字可以改变，代表训练的次数
    update(test=True)
    print('Qtable:')
    print(RL.Qtable)