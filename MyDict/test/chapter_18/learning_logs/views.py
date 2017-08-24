from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Learning Log."""
    # ## 学习主页的日志。
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    # ## 显示所有主题。
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    # ## 显示单个主题,及其所有条目。
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
