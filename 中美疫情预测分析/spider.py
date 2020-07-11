# -*- coding:utf-8 -*-
# @Time: 2020/5/30 21:10
# @Author: R.X.L
# @File: spider.py
import requests
import re
import pandas as pd
import json
from bs4 import BeautifulSoup

def getHTML():
    url = 'https://ncov2019.live/data/unitedstates'
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    doc = r.text
    soup = BeautifulSoup(doc, 'html.parser')
    return soup

def analyzeHTML(soup):
    x = soup.find_all(name='script',
                      attrs={'type': 'text/javascript'},
                      string=re.compile('report'))
    report = str(x)
    report = report[48:-13]
    report = json.loads(report)
    return report

def showTime(report):
    time = report['last_updated']
    return time
    # print(time)

def addColumn(report):
    data = report['regions']['world']['list']
    all = report['regions']['world']['totals']
    state_data = report['regions']['unitedstates']['list']
    df = pd.DataFrame(data)
    all_df = pd.DataFrame([all])
    state_data_df = pd.DataFrame(state_data)
    new_col = all_df.columns.insert(0, 'country')
    all_df = all_df.reindex(columns=new_col)
    all_df.loc[:, 'country'] = ['World']
    return [all_df,df,state_data_df]
# print(state_data_df)
# print(df)
# print(all_df)
def saveData(all_df, df, state_data_df,t):
    # time = showTime(report)
    time = t
    try:
        all_df.to_excel(r'G:\疫情数据\WorldData\世界总数据'+time[5:10]+'.xls', index=False)
        df.to_excel(r'G:\疫情数据\CountryData\各国数据'+time[2:10]+'.xls', index=False)
        state_data_df.to_excel(r'G:\疫情数据\USData\美国各州数据'+time[2:10]+'.xls', index=False)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    soup = getHTML()
    report = analyzeHTML(soup)
    Data = addColumn(report)
    t = showTime(report)
    saveData(Data[0],Data[1],Data[2],t)
    print(t)


