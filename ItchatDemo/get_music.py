import requests
import urllib.request
import json

word = "周杰伦"
res1 = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=' + word)
jm1 = json.loads(res1.text.strip('callback()[]'))
jm1 = jm1['data']['song']['list']

mids = []
songmids = []
srcs = []
songnames = []
singers = []

for j in jm1:
    try:
        mids.append(j['media_mid'])
        songmids.append(j['songmid'])
        songnames.append(j['songname'])
        singers.append(j['singer'][0]['name'])
    except:
        print('wrong')

for n in range(0,len(mids)):
    res2 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+songmids[n]+'&filename=C400'+mids[n]+'.m4a&guid=6612300644')
    jm2 = json.loads(res2.text)
    # print(jm2)
    vkey = jm2['data']['items'][0]['vkey']
    srcs.append('http://dl.stream.qqmusic.qq.com/C400'+mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66')

# print(srcs[0])
print('开始下载：' + word)

for x in srcs:
    print(x)

# x = len(srcs)
#
# for m in range(0,x):
#     print(str(m) + '*****' + songnames[m] + '-' + singers[m] + ".m4a *****" + '下载中')
#     try:
#         urllib.request.urlretrieve(srcs[m],'D:/music/' + songnames[m] + '-' + singers[m] + '.m4a')
#     except Exception as e:
#         x = x - 1
#         print('download wrong' + e)
# print(word + '歌曲下载完毕')