from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from .models import Task

class TaskNotificationObserver:
    def notify(self, message):
        print(f"Notification:{message}")

@receiver(post_save,sender=Task)
def notify_task_created(sender,instance,created,**kwargs):
    print("signal triggered")
    observer=TaskNotificationObserver()
    if created:
        observer.notify(f"New Task added: {instance.title}")
    else:
        observer.notify(f"Task updated: {instance.title}") 

@receiver(post_delete, sender=Task)
def notif_task_deleted(sender,instance,**kwargs):
    observer=TaskNotificationObserver()
    observer.notify(f"Task deleted: {instance.title}")           