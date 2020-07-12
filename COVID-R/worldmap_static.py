# -*- coding:utf-8 -*-
# @Time: 2020/7/11 17:59
# @Author: R.X.L
# @File: worldmap_static.py

import json
from pyecharts import options as opts
from pyecharts.charts import  Map
confirmed = []
# 读取数据
path = r'G:\新建文件夹\covid19-master\docs\timeseries.json'
f = open(path, mode='r', encoding='utf-8')
dt = json.load(f)
dt['United States'] = dt.pop('US')
# print(dt)
# 所有国家的名字
country_name = dt.keys()
country_name = list(country_name)
# print(type(country_name))
for i in country_name:
    confirmed.append(dt[i][-1]['confirmed'])
# print(confirmed)

c = (
    Map()
    # Map(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add("累计确诊人数", [list(z) for z in zip(country_name, confirmed)], "world",
         is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=100000),
    )
    .render("世界地图累计确诊.html")
)


