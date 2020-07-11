# -*- coding:utf-8 -*-
# @Time: 2020/7/11 17:59
# @Author: R.X.L
# @File: worldmap_static.py

import json
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Timeline, Map

'''
构造了3个数据结构，分别是date_list、cy_name_list 和 ncov_data。
date_list存放的是日期列表，因为我们画动图，所以需要一段时间；
cy_name_list 存放收集的所有国家列表（英文名）；
ncov_data是一个字典，key是日期，value是数组，存放各个国家当天的确诊病例数。
'''

confirmed = []
# 读取数据
path = r'G:\新建文件夹\covid19-master\docs\timeseries.json'
f = open(path, mode='r', encoding='utf-8')
dt = json.load(f)

# 所有国家的名字
country_name = dt.keys()
country_name = list(country_name)
# print(type(country_name))
# for i in country_name:
#     confirmed.append(dt[i][-1]['confirmed'])
# print(confirmed)



c = (
    Map(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add("累计确诊人数", [list(z) for z in zip(country_name, confirmed)], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=400),
    )
    .render("世界地图.html")
)


