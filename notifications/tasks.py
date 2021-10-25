from __future__ import absolute_import, unicode_literals
from celery import shared_task

import time
from . import models

@shared_task
def update_table():
    new_obj = models.Blog.objects.all()
    for i in new_obj:
        i.active = True
        i.save()
        time.sleep(60)

