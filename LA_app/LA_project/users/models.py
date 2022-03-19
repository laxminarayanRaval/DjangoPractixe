from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # decorators for signals

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/avtar.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twiter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

class Skills(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=Profiles)
def profileUpdated(sender,instance, created, **kwargs):
    print("Profile SAved")
    print("Instance:", instance)
    print("Created :", created)

def profileDelete(sender, instance, **kwargs):
    print("Profile Deleted")

# post_save.connect(profileUpdated, sender=Profiles)
# post_delete.connect(profileDelete, sender=Profiles)