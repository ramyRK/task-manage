from django.mb.models.signals import post_save
from django.dispatch import receiver
from .models import Task

class TaskNotificationObserver:
    def notify(self, message):
        print(f"Notification:{message}")

@receiver(post_save,sender=Task)
def notify_task_created(sender,instancen,created,**kwargs):
    observer=TaskNotificationObserver()
    if created:
        observer.notify(f"New Task added: {instance.title}")
    else:
        observer.notify(f"Task updated: {instance.title}") 