from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TimeStampedModel(models.Model):
    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ProjectType(TimeStampedModel):
    type = models.CharField(max_length=255)
    slug = models.SlugField(default="", null=False)
    desc = models.CharField(max_length=255, blank=True)
    status= models.BooleanField(default=True)
    def __str__(self):
        return self.type

class Client(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False)
    country = models.CharField(max_length=150, blank=True)
    desc = models.TextField(blank=True)
    image = models.CharField(blank=True, max_length=255)
    status= models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="", null=False)
    detail = models.TextField(blank=True)
    deadline = models.DateTimeField()
    image = models.CharField(blank=True, max_length=255)
    projectType = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class Task(TimeStampedModel):
    task = models.CharField(max_length=255)
    slug = models.SlugField(default="", null=False)
    detail = models.TextField(blank=True)
    startDateT = models.DateTimeField()
    endDateT = models.DateTimeField()
    image = models.CharField(blank=True, max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    complete= models.BooleanField(default=False)
    def __str__(self):
        return self.task
    
class Message(TimeStampedModel):
    Task_Status = [("INITIAL","INITIAL"), ("Reply","Reply")]


    subject =models.CharField(max_length=250)
    message = models.TextField()
    attachment =models.CharField(max_length=250)
    messageType = models.CharField(max_length=30, choices=Task_Status)
    sender = models.ForeignKey(User,related_name='message_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='message_receiver', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, related_name='parent_message',null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.subject
    
    