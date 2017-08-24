"""Defines url patterns for users."""
# ## 为用户定义的url模式。

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login page.
    # ## 登录页面。
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
        
    # Logout page.
    # ## Logout页。
    url(r'^logout/$', views.logout_view, name='logout'),
    
    # Registration page. 
    # ## 岳父页。
    url(r'^register/$', views.register, name='register'),
]
