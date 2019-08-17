# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:37:22 2019

@author: Administrator
"""
import pandas as pd
import numpy as np
import random
n_status=5
class QLearningTable():
    def __init__(self):
        self.actions=['left','right']
        self.n_status=n_status
        self.egreedy=0.95#这个概率选最优
        self.lr=0.1
        self.decay=1
        self.terminal=self.n_status-1#设定结束的点
        self.Qtable=pd.DataFrame(data=np.zeros((self.n_status,len(self.actions))),columns=self.actions)#初始值为0
    def choose_action(self,observation):
        if random.random()<self.egreedy:
            values=self.Qtable.iloc[observation]
            action=random.choice(self.Qtable.iloc[observation][self.Qtable.iloc[observation]==(values.max())].index)
        else:
            action=random.choice(self.Qtable.iloc[observation].index)#剩余概率，随机选取
        return action
            
    def learn(self,observation,observation_,action,reward):
        #更新Qtable
        if observation_!=self.terminal:
            real=self.Qtable.iloc[observation_].max()*self.decay+reward
        else:
            real=reward
        predict=self.Qtable[action].iloc[observation]
        self.Qtable[action].iloc[observation]=predict+self.lr*(real-predict)

class Environment():
    def __init__(self):
        self.n_status=n_status
        self.hunter='1'
        self.location=0#第一个点序号为0
        self.steps=0#目前还没走
    def reset(self):#返回初始状态
        self.steps=0
        self.location=0
        print(self.hunter+(self.n_status-1)*'.')
        return self.location#返回初始状态的值
    def render(self):#更新string,并显示
        a=list(self.n_status*'.')
        a[self.location]='1'
        print(''.join(a))
    def step(self,action):
        reward=0#先预置为0
        done=False
        if action=='left':
            self.location=max(0,self.location-1)
        else:
            self.location=min(self.n_status-1,self.location+1)#n_status-1是最大索引
        if self.location==self.n_status-1:#走到最后一格
            reward=1
            done=True
        self.steps=self.steps+1
        return  self.location,reward,done
        
        
        