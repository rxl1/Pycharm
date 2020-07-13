# -*- coding:utf-8 -*-
# @Time: 2020/7/10 13:15
# @Author: R.X.L
# @File: Logistic.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
matplotlib.rcParams['font.family']=['SimHei']

def logistic_increase_function(t, K, P0, r):
    # t0 = 11
    t0 = 1
    # r 0.05/0.55/0.65
    r = 0.03
    # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

'''
1.11日41例
1.18日45例
1.19日62例
1.20日291例
1.21日440例
1.22日571例
1.23日835例
1.24日1297例
1.25日1985例
1.26日2762例
1.27日4535例
'''

#  日期及感染人数
# t = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
# t = [1,2,3,4,5,6,7,8,9,10,11,12,13]
t = [1,2,3,4,5,6,7,8,9,10]
t = np.array(t)
# P = [41, 45, 62, 291, 440, 571, 835, 1297, 1985, 2762, 4535]
# P = [2727996,2779953,2837189,2890588,2935770,2982928,
#      3041035,3097084,3158932,3219999,3291786,3355646,3413995]
P = [2727996,2779953,2837189,2890588,2935770,2982928,
     3041035,3097084,3158932,3219999]
P = np.array(P)

# 用最小二乘法估计拟合
# 现有数据曲线拟合检验
popt1, pcov1 = curve_fit(logistic_increase_function, t,P)

# 获取popt里面是拟合系数
# print("K:capacity  P0:initial_value   r:increase_rate   t:time")
# print("K:容量  P0:初始值   r:增长率   t:日期")
# print(popt1)

# 拟合后预测的P值
P_predict = logistic_increase_function(t, popt1[0], popt1[1], popt1[2])
# print(P_predict)

# 未来预测
# future = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 41, 51, 61, 71, 81, 91, 101]
future= []
for i in range(1,11):
    future.append(i)
future = np.array(future)
future_predict = logistic_increase_function(future, popt1[0], popt1[1], popt1[2])

# 近期情况预测
# tomorrow = [28, 29, 30, 32, 33, 35, 37, 40]
tomorrow = []
for i in range(11,30):
    tomorrow.append(i)
# tomorrow = [14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
tomorrow = np.array(tomorrow)
tomorrow_predict = logistic_increase_function(tomorrow, popt1[0], popt1[1], popt1[2])
print(tomorrow_predict)
# 绘图
plot1 = plt.plot(t, P, 'o', label="确认感染人数")
plot2 = plt.plot(t, P_predict, 'r', label='预测感染人数')
plot3 = plt.plot(tomorrow, tomorrow_predict, 'go-', label='近期确诊人数预测')
plt.xlabel('日期')
plt.ylabel('确诊人数')
plt.legend(loc=0)  # 指定legend的位置右下角
plt.show()
# print(logistic_increase_function(np.array(28), popt1[0], popt1[1], popt1[2]))
# print(logistic_increase_function(np.array(29), popt1[0], popt1[1], popt1[2]))
