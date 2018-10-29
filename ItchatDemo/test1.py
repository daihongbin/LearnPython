# 微信工具库
import itchat
#画图的库，Bar柱状图，Pie饼状图，Map地图
from pyecharts import Pie,Map,Bar

#数据库
import pymysql

itchat.login() #生成二维码，登陆微信

# 发送文件
'''image_1 = r'D:\用户目录\我的图片\Jax.jpg'
image_2 = r'D:\用户目录\我的图片\0.jpg'

itchat.send_image(image_1,'filehelper')
itchat.send_image(image_2,'filehelper')'''

#获取好友信息
friends = itchat.get_friends(update = True)[:]

#总好友数，减去自己
total = len(friends) - 1
print('好友人数',total)

# 爬去的各个参数
result = [('RemarkName','备注'),('NickName','微信昵称'),
          ('Sex','性别'),('City','城市'),('Province','省份'),
           ('UserName','用户名'),('Signature','个性签名')]

male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
"不明性别好友： %.2f%%" % (float(other) / total * 100))

pie = Pie('震惊！原来树根微信好友是这样的')
pie.add(' ',['男','女','外星人'],[(float(male)/total*100),(float(female) / total * 100),(float(other) / total * 100)])
#pie.render()

bar = Bar('震惊！原来树根微信好友是这样的')
bar.add(' ',['男','女','外星人'],[(float(male)/total*100),(float(female) / total * 100),(float(other) / total * 100)])
#bar.render()

# 定义函数，用于得到各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)

    return variable

NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')

from pandas import  DataFrame
data = {'NickName':NickName,'Sex':Sex,'Province':Province,'City':City,'Signature':Signature}
frame = DataFrame(data)

city_name = []
for i in list(frame['City']):
    j = '%s%s' % (i,'市')
    city_name.append(j)

import numpy as np
City_name = ['朝阳市', '潮州市', '东莞市', '佛山市', '广州市', '河源市',
             '惠州市', '汕头市', '江门市', '揭阳市', '茂名市', '梅州市',
             '清远市', '汕尾市', '韶关市', '深圳市', '肇庆市',
             '湛江市', '云浮市', '中山市', '珠海市', "阳江市"]

num = []
for i in City_name:
    num.append(city_name.count(i))

cc = Map('树根的微信好友分布（仅广东）',width=1200,height=600)
cc.add('',City_name,num,maptype='广东',is_visualmap=True,visual_range=[0,150],visual_text_color='#000')
cc.render()

