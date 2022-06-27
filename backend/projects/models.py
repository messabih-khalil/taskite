from django.db import models

# import signals 



# Create your models here.

# Project Model

CHOICES=[('new','New'),
         ('inProgress','in progress'),
         ('done','Done'),
         ]
class Project(models.Model):
    admin = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE)
    title = models.CharField(blank=False , null=False , max_length=200)
    description = models.TextField(blank=True , null=True)
    team = models.ManyToManyField("accounts.NewUser" , related_name="team_friends")  
    status = models.CharField(choices=CHOICES, default="new" , max_length=20,)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title