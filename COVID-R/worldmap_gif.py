# -*- coding:utf-8 -*-
# @Time: 2020/7/11 17:58
# @Author: R.X.L
# @File: worldmap_gif.py

import json
from pyecharts import options as opts
from pyecharts.charts import Timeline, Map

'''
构造了3个数据结构，分别是date_list、cy_name_list 和 ncov_data。
date_list存放的是日期列表，因为我们画动图，所以需要一段时间；
cy_name_list 存放收集的所有国家列表（英文名）；
ncov_data是一个字典，key是日期，value是数组，存放各个国家当天的确诊病例数。
'''
date_list = []
confirmed = []
confirmed_dict={}
value = []

# 读取数据
path = r'G:\新建文件夹\covid19-master\docs\timeseries.json'
f = open(path, mode='r', encoding='utf-8')
dt = json.load(f)
dt['United States'] = dt.pop('US')

# 所有国家的名字
country_name = dt.keys()
country_name = list(country_name)
# print(type(country_name))
# for i in country_name:
#     confirmed.append(dt[i][-1]['confirmed'])
# print(confirmed)

# 处理时间
for i in dt['United States']:
    date_list.append( i['date'] )

# 处理字典里的数据
i = 0
while i <len(date_list):
    for j in country_name:
        x = dt[j]
        value.append(x[i]['confirmed'])
    confirmed_dict[date_list[i]] = value
    value = []
    i = i+1
# print(type(confirmed_dict))
# print(confirmed_dict['2020-5-25'])

# 画图
tl = Timeline() # 创建时间线轮播多图，可以让图形按照输入的时间动起来
     # is_auto_play：自动播放
    #  play_interval：播放时间间隔，单位：毫秒
    #  is_loop_play：是否循环播放
tl.add_schema(is_auto_play=True, play_interval=100, is_loop_play=True)

for date_str in date_list:  # 遍历时间列表
    map0 = (
        Map()  # 创建地图图表
            # 将国家名 cy_name_list 以及各国当天确诊病例 ncov_data[date_str] 加入地图中
        .add("全球疫情趋势", [list(z) for z in zip(country_name, confirmed_dict[date_str])],
                 "world", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 不显示国家名
        .set_global_opts(
            title_opts=opts.TitleOpts(title="%s日" % date_str),  # 图表标题
            visualmap_opts=opts.VisualMapOpts(max_=80),   # 当确诊病例大于80 ，地图颜色是红色
            )
        )
    tl.add(map0, "%s" % date_str)  # 将当天的地图状态加入时间线中
tl.render('世界地图动态累计确诊.html')  # 生成最终轮播多图，会在当前目录创建 render.html 文件





