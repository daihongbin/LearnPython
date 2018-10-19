"""zqxt_tmpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from learn import views as learn_views

urlpatterns = [
    url(r'^home5/$',learn_views.home5,name='home5'),
    url(r'^jiafa/(\d+)/(\d+)/$',learn_views.add,name='add'),
    #url(r'^add/(\d+)/(\d+)/$',learn_views.add,name='add'),
    url(r'^home4/$',learn_views.home4,name='home4'),
    url(r'^home3/$',learn_views.home3,name='home3'),
    url(r'^home2/$',learn_views.home2,name='home2'),
    url(r'^home1/$',learn_views.home1,name='home1'),
    url(r'^template/$',learn_views.template,name='template'),
    url(r'^$',learn_views.home,name='home'),
    url(r'^admin/', admin.site.urls),
]
