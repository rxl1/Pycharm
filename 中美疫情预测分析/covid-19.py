# -*- coding:utf-8 -*-
# @Time: 2020/7/7 14:57
# @Author: R.X.L
# @File: covid-19.py
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import pyecharts.options as opts
from pyecharts.charts import Line
matplotlib.rcParams['font.family']=['SimHei']  # matplotlib正确显示中文

'''
数据来源: https://github.com/pomber/covid19
统计截至日期: 20-07-05
pyecharts库要使用1.7.1版本，官方文档给的都是此版本
'''

# 读取文件并返回
def read_File():
    path = r'G:\新建文件夹\covid19-master\docs\timeseries.json'
    f = open(path, mode='r', encoding='utf-8')
    dt = json.load(f)
    return dt

# 获取美国数据，返回DataFrame类型
def get_us_data(dt):
    us_dt = dt['US']
    us_df = pd.DataFrame(columns=('date', 'confirmed', 'deaths', 'recovered'))
    for i in us_dt:
        us_df = us_df.append([{'date': i['date'], 'confirmed': i['confirmed'],
                               'deaths': i['deaths'], 'recovered': i['recovered']}])
    return us_df

# 获取中国数据，返回DataFrame类型
def get_china_data(dt):
    china_dt = dt['China']
    china_df = pd.DataFrame(columns=('date', 'confirmed', 'deaths', 'recovered'))
    for i in china_dt:
        china_df = china_df.append([{'date': i['date'], 'confirmed': i['confirmed'],
                               'deaths': i['deaths'], 'recovered': i['recovered']}])
    return china_df

# matplotlib 作折线图（这个并不好）
def plot_us(us_df):
    confirmed = us_df['confirmed'].tolist()
    deaths = us_df['deaths'].tolist()
    recovered = us_df['recovered'].tolist()
    time = us_df['date'].tolist()
    date = []
    for i in time:
        index = i.split('-')
        month = index[1]
        day = index[2]
        date.append(datetime.strptime('2020-%s-%s'% (month,day),'%Y-%m-%d'))
    plt.xlabel('日期')
    plt.ylabel('人数')
    plt.title('美国新冠肺炎确诊人数趋势图')
    plt.grid('True')  # 显示网格
    plt.plot(date, confirmed, 'b',
             date, recovered, 'c',
             date, deaths, 'r')
    plt.xticks(rotation=35)  # 横坐标倾斜度数
    plt.figure(figsize=(20,20),dpi=800)
    plt.show()

# pyecharts作累计折线图（效果不错）
def line_us(us_df):
    confirmed = us_df['confirmed'].tolist()
    deaths = us_df['deaths'].tolist()
    recovered = us_df['recovered'].tolist()
    time = us_df['date'].tolist()
    date = []
    for i in time:
        index = i.split('-')
        month = index[1]
        day = index[2]
        date.append('20-'+str(month)+'-'+str(day))  #使日期不再显示几时几分几秒
        # date.append(datetime.strptime('2020-%s-%s' % (month, day), '%Y-%m-%d'))
    (
        Line(init_opts=opts.InitOpts(width="1000px", height="600px"))
            .add_xaxis(xaxis_data=date)
            .add_yaxis(
                series_name="累计确诊",
                y_axis=confirmed,
        )
            .add_yaxis(
                series_name="累计死亡",
                y_axis=deaths,
        )
            .add_yaxis(
                series_name="累计治愈",
                y_axis=recovered,
        )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="美国疫情趋势", subtitle="R.X.L。"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,name='日期',min_=3),
                yaxis_opts=opts.AxisOpts(name='人数', min_=3)
        )
            .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        )
            .render("美国累计人数.html")
    )

# pyecharts作新增折线图
def line_us_newadd(us_df):
    new_confirmed = []
    new_deaths = []
    new_recovered = []
    x = 1
    confirmed = us_df['confirmed'].tolist()
    deaths = us_df['deaths'].tolist()
    recovered = us_df['recovered'].tolist()
    while (x < len(confirmed)):
        new_confirmed.append(confirmed[x] - confirmed[x-1])
        new_deaths.append(deaths[x]- deaths[x-1])
        new_recovered.append(recovered[x] - recovered[x-1])
        x = x + 1
    time = us_df['date'].tolist()
    date = []
    for i in time:
        index = i.split('-')
        month = index[1]
        day = index[2]
        date.append('20-' + str(month) + '-' + str(day))  # 使日期不再显示几时几分几秒
    date = date[1:]
    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=date)
            .add_yaxis(
                series_name="新增确诊",
                y_axis=new_confirmed,
        )
            .add_yaxis(
                series_name="新增死亡",
                y_axis=new_deaths,
        )
            .add_yaxis(
                series_name="新增治愈",
                y_axis=new_recovered,
        )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="美国疫情趋势", subtitle="R.X.L。"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                         name='日期',min_=3
                                         # axislabel_opts=opts.LabelOpts(rotate=-30)  # x轴横坐标倾斜度
                                         ),
                yaxis_opts=opts.AxisOpts(name='人数', min_=3)
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False) , # 隐藏数字
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5)  #设置面积
            )
            .render("美国新增人数.html")
    )

def geo_us():
    pass

if __name__=='__main__':
    dt = read_File()
    us_df = get_us_data(dt)
    china_df = get_china_data(dt)
    # plot_us(us_df)
    line_us(us_df)
    line_us_newadd(us_df)







# path = r'G:\新建文件夹\covid19-master\docs\timeseries.json'
# f = open(path,mode='r',encoding='utf-8')
# dt = json.load(f)
# us_dt = dt['US']
# us_df = pd.DataFrame(columns=('date','confirmed','deaths','recovered'))
# for i in us_dt:
#     us_df = us_df.append([{'date':i['date'],'confirmed':i['confirmed'],
#                            'deaths':i['deaths'],'recovered':i['recovered']}])
# print(us_df)
# print(us_df)
# print(type(us_dt))
# print(len(us_dt))
# print(us_dt[0])
# print(us_dt[0]['date'])
# print(type(us_dt[0]))