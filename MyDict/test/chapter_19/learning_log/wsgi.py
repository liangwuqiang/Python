"""
WSGI config for learning_log project.
# ## WSGI learning_log项目配置。

It exposes the WSGI callable as a module-level variable named ``application``.
# ## 它使WSGI可调用的模块级变量命名为“应用程序”。

For more information on this file, see
# ## 关于这个文件的更多信息,请参阅
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
# ## https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

application = get_wsgi_application()
