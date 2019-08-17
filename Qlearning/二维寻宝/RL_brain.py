# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:37:22 2019

@author: Administrator
"""
import pandas as pd
import numpy as np
import random
rows=6#行数
columns=6#列数
location=(0,0)
treasure=(4,4)
trap=[(3,3),(2,3)]
class QLearningTable():
    def __init__(self):
        self.actions=['left','right','up','down']
        self.n_status=1#当前Q表中存的状态数
        self.egreedy=0.8#这个概率选最优
        self.lr=0.1
        self.decay=0.9
        self.treasure=treasure
        self.trap=trap
        self.location=location
        self.Qtable=pd.DataFrame(data=np.zeros((self.n_status,len(self.actions))),columns=self.actions,index=[str(self.location)])#初始值为0
    def choose_action(self,observation):
        if random.random()<self.egreedy:
            values=self.Qtable.loc[observation]
            action=random.choice(self.Qtable.loc[observation][self.Qtable.loc[observation]==(values.max())].index)
        else:
            action=random.choice(self.Qtable.loc[observation].index)#剩余概率，随机选取
        return action
            
    def learn(self,observation,observation_,action,reward):
        #更新Qtable
        if observation_ not in [str(tr) for tr in self.trap] and observation_ !=str(self.treasure):
            real=self.Qtable.loc[observation_].max()*self.decay+reward
        else:
            real=reward
        predict=self.Qtable[action].loc[observation]
        self.Qtable[action].loc[observation]=predict+self.lr*(real-predict)
        
    def check_exist(self,observation):
        if observation not in self.Qtable.index:#则补充
            self.Qtable.loc[observation]=(0,0,0,0)
            

class Environment():
    def __init__(self):
        self.rows=rows
        self.columns=columns
        self.hunter='1'
        self.location=location
        self.steps=0#目前还没走
        self.treasure=treasure
        self.trap=trap

    def reset(self):#返回初始状态
        self.steps=0
        self.location=(0,0)
        return str(self.location)#返回初始状态的值
    def render(self):#用于显示可视化界面
        all_map=np.zeros((self.rows,self.columns))
        for i in range(self.rows):
            for j in range(self.columns):
                if (i,j)==self.treasure:
                    all_map[i,j]=1
                elif (i,j) in self.trap:
                    all_map[i,j]=-1
                elif (i,j)==self.location:
                    all_map[i,j]=5
        for i in range(self.rows):
            for j in range(self.columns):
                if all_map[i,j]==0:
                    print('*  ',end='')
                elif all_map[i,j]==1:
                    print('O  ',end='')
                elif all_map[i,j]==-1:
                    print('X  ',end='')
                else:
                    print('1  ',end='')#print完毕
            print('\n')
        print('——————————————————————————————————————————————')
        
        
    def step(self,action):
        reward=0#先预置为0
        done=False
        if action=='left':
            self.location=(self.location[0],max(0,self.location[1]-1))
        elif action=='right':
            self.location=(self.location[0],min(self.columns-1,self.location[1]+1))
        elif action=='up':
            self.location=(max(0,self.location[0]-1),self.location[1])
        elif action=='down':
            self.location=(min(self.rows-1,self.location[0]+1),self.location[1])

        if self.location==self.treasure:#找到宝藏
            reward=1
            done=True
        elif self.location in self.trap:
            reward=-1
            done=True
        self.steps=self.steps+1
        return  str(self.location),reward,done

        
        
        