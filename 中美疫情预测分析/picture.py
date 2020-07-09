# -*- coding:utf-8 -*-
# @Time: 2020/7/5 14:29
# @Author: R.X.L
# @File: picture.py
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']=['SimHei']

path = 'G:\疫情数据\CountryData'
dir = os.listdir(path)
US_confirmed=[]
US_deaths=[]
US_recovered=[]
date=[]
i=0
while i < len(dir):
    df = pd.read_excel(path+os.sep+dir[i])
    df = df[df['country']=='United States']

    month = df.last_updated
    month = str(month)
    month = month[12:14]

    day = df.last_updated
    day = str(day)
    day = day[15:17]

    a = int(df.confirmed)
    b = int(df.deaths)
    c = int(df.recovered)

    US_confirmed.append(a)
    US_deaths.append(b)
    US_recovered.append(c)
    date.append(datetime.strptime('2020-%s-%s' % (month, day),'%Y-%m-%d'))
    # date.append(someday.strptime('%Y-%m-%d'))
    i = i+1
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # 格式化时间轴标注
# plt.gcf().autofmt_xdate() # 优化标注（自动倾斜）
# plt.grid(linestyle=':') # 显示网格
# plt.legend(loc='best') # 显示图例
plt.xlabel('日期')
plt.ylabel('人数')
plt.title('美国新冠肺炎确诊人数趋势图')
plt.grid('True')
plt.plot(date,US_confirmed,'b',
         date,US_recovered,'c',
         date,US_deaths,'r')
# plt.plot(date,US_confirmed,'rs')
# plt.plot(date,US_recovered,'c')
# plt.plot(date,US_recovered,'b*')
# plt.plot(date,US_deaths,'r')
# plt.plot(date,US_deaths,'y+')
plt.xticks(rotation=60)
plt.show()

