from django.db import models
# Create your models here.

# task status choices
CHOICES=[('new','New'),
         ('inProgress','in progress'),
         ('done','Done'),
         ]
class Task(models.Model):
    user = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE)
    title = models.CharField(blank=False , null=False , max_length=200)
    description = models.TextField(blank=True , null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(choices=CHOICES, default="new" , max_length=20,)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# SubTask model

class SubTask(models.Model):
    user = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project" , on_delete=models.CASCADE)
    title = models.CharField(blank=False , null=False , max_length=200)
    description = models.TextField(blank=True , null=True)
    status = models.CharField(choices=CHOICES, default="new" , max_length=20,)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title