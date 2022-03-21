from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # decorators for signals

from django.contrib.auth.models import User
from .models import Profiles


# @receiver(post_save, sender=Profiles)
# def profileUpdated(sender,instance, created, **kwargs):
    # print("Profile SAved")
    # print("Instance:", instance)
    # print("Created :", created)

def createProfile(sender, instance, created, **kwargs):
    print("Profile Created")
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

# def profileDelete(sender, instance, **kwargs):
    # print("Profile Deleted")

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    print("Profile Deleted")
    user.delete()

# post_save.connect(profileUpdated, sender=Profiles)
# post_delete.connect(profileDelete, sender=Profiles)

post_save.connect(createProfile, sender=Profiles)
post_delete.connect(deleteUser, sender=Profiles)