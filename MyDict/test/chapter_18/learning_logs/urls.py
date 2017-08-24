"""Defines url patterns for learning_logs."""
# ## 定义了learning_logs url模式。

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    # ## 主页。
    url(r'^$', views.index, name='index'),
    
    # Show all topics.
    # ## 显示所有主题。
    url(r'^topics/$', views.topics, name='topics'),
    
    # Detail page for a single topic.
    # ## 单个主题的详细信息页面。
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
