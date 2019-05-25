"""helppod URL Configuration

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

from insight.views import home,login_view, post_task ,task_list,task_detail,accept,signup_view ,success ,helper_success, choose_signup ,helpsignup_view,logout_view,contact_us

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home , name='home'),
    url(r'^login/$', login_view , name='login'),
    url(r'^csignup/$', choose_signup, name='csignup'),
    url(r'^hsignup/$', helpsignup_view, name='hsignup'),
    url(r'^signup/$', signup_view , name='signup'),
    url(r'^post/$', post_task , name= 'post'),
    url(r'^list/$', task_list , name= 'list'),
    url(r'^success/$', success, name= 'success'),
    url(r'^contact/$', contact_us, name= 'contact'),
    url(r'^hsuccess/$', helper_success, name= 'hsuccess'),
    url(r'^(?P<id>\d+)/detail/$', task_detail,name='detail'),
    url(r'^(?P<id>\d+)/accept/$', accept ,name='accept'),
    url(r'^logout/$', logout_view , name='logout'),

]
