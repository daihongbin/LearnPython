from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

# 显示一个基本的字符串在网页上
def home1(request):
    string = u"学习Django，并用来构建网站"
    return render(request,'home1.html',{'string':string})

# 基本的for循环和list内容的显示
def home2(request):
    TutorialList = ["HTML","CSS","jQuery","Python","Django"]
    return render(request,'home2.html',{'TutorialList':TutorialList})

# 显示字典中内容
def home3(request):
    info_dict = {'site':u'zqxt','content':u'呵呵呵'}
    return render(request,'home3.html',{'info_dict':info_dict})

# 在模板进行条件判断和for循环的操作
def home4(request):
    List = map(str,range(100)) # 一个长度为100的List
    return render(request,'home4.html',{'List':List})

# 模板上得到对应视图的网址
def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def template(request):
    return render(request,'template.html')

# 模板中的逻辑操作
def home5(request):
    a = 5
    strList = ['1213','1231']
    return render(request,'home5.html',{'a':5,'strList':strList})

# 获取当前网址，当前用户
def home6(request):
    return render(request,'homt5.html')
