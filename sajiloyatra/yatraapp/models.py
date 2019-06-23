from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Food(models.Model):
    food_image_url = models.CharField(max_length=600)
    location = models.CharField(max_length=50)
    food_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200, null=True)
    category = models.CharField(max_length = 500)
    month = models.CharField(max_length=70)

    def __str__(self):
        return self.food_name

    # class Meta:
        # db_table = 'yatraapp__food'
        # get_latest_by = 'checkout'
        # order_with_respect_to = 'location'


class Festival(models.Model):
    festival_image_url = models.CharField(max_length=600)
    location = models.CharField(max_length=50)
    festival_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)
    ethinic = models.CharField(max_length=100)
    month = models.CharField(max_length=60)

    def __str__(self):
        return self.festival_name


class EventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class CompletedEvents(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=False)


class EventVerified(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_verified=True)


class Event(models.Model):
    location = models.CharField(max_length=50, null=True)
    event_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    month = models.CharField(max_length=60, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    objects = EventManager()
    completed_objects = CompletedEvents()
    verified = EventVerified()


class EventCompletion(models.Model):
    location = models.CharField(max_length=50, null=True)
    event_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    month = models.CharField(max_length=60, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    objects = EventManager()
    is_verified = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Planner(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class FoodReview(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=500)
    review = models.TextField()

    def __str__(self):
        return self.reviewer

class FestivalReview(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=500)
    review = models.TextField()

    def __str__(self):
        return self.reviewer



