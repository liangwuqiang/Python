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
    
    # Page for adding a new topic.
    # ## 页面添加一个新话题。
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry.
    # ## 页面添加一个新条目。
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    # Page for editing an entry.
    # ## 页面编辑条目。
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
