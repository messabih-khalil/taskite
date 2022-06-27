from django.db import models

from accounts.models import NewUser

# import signals 
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
# Create your models here.

# friend status choices
CHOICES=[('accept','Accept'),
         ('inProgress','In Progress'),
         ]


class Friend(models.Model):
    user = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE)
    friend = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE , related_name="friend_user")

    status_friend = models.CharField(choices=CHOICES, default="inProgress" , max_length=20,)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user_name + ":" + self.friend.user_name


class Invitation(models.Model):
    user = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE)
    invitation_from = models.ForeignKey("accounts.NewUser" , on_delete=models.CASCADE , related_name="friend_invitaion_user")

    invitation_status = models.CharField(choices=CHOICES, default="inProgress" , max_length=20,)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user_name + ":" + self.invitation_from.user_name

 
# Create invitation

    
@receiver(post_save, sender=Friend)
def create_invitation(sender, instance, created, **kwargs):
    if created:
        user = NewUser.objects.get(user_name = instance.friend.user_name)
        invitation_from = NewUser.objects.get(user_name = instance.user.user_name)
        inv = Invitation.objects.create(user = user , invitation_from=invitation_from)
        inv.save()

