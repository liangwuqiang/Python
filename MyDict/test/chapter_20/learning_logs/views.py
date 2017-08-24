from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    # ## 学习主页的日志。
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    # ## 显示所有主题。
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    # ## 显示单个主题,及其所有条目。
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    # ## 确保这个话题属于当前用户。
    if topic.owner != request.user:
        raise Http404
        
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    # ## 添加一个新的话题。
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # ## 没有提交的数据;创建一个空白的表格。
        form = TopicForm()
    else:
        # POST data submitted; process data.
        # ## POST数据提交;流程数据。
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # ## 为一个特定的主题添加一个新条目。
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # ## 没有提交的数据;创建一个空白的表格。
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        # ## POST数据提交;流程数据。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # ## 编辑现有条目。
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        # ## 初始请求;预先填充表单与当前条目。
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        # ## POST数据提交;流程数据。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
