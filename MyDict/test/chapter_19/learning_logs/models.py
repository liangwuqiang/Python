from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about."""
    # ## 主题用户学习。
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        # ## 返回一个字符串表示的模型。
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    # ## 具体了解了主题的东西。
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        """Return a string representation of the model."""
        # ## 返回一个字符串表示的模型。
        return self.text[:50] + "..."
