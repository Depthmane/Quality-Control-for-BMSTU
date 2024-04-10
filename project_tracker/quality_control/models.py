from django.db import models

from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True, )
    STATUS_CHOICES = [
        ("New", "Новая"),
        ("In progress", "В работе"),
        ("Completed", "Завершена"),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="new",
    )
    PRIORITY_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    priority = models.IntegerField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True, )
    STATUS_CHOICES = [
        ("Consideration", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Declined", "Отклонено"),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="new",
    )
    PRIORITY_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    priority = models.IntegerField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
