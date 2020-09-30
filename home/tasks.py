from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from datetime import date
import os
from django.conf import settings
from celery import shared_task, task
from datetime import timedelta



@task(reject_on_worker_lost=True)
def add(a,b):
    print("Task is starting")
    return a + b


@periodic_task(run_every=timedelta(seconds=15))
def scheduled_task():
    print("Task is done")
