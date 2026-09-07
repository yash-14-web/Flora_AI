from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    MEASUREMENT_CHOICES = [
        ('Metric', 'Metric (Celsius, Hectares)'),
        ('Imperial', 'Imperial (Fahrenheit, Acres)'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=150, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    crop_focus = models.CharField(max_length=255, blank=True)
    measurement_unit = models.CharField(max_length=20, choices=MEASUREMENT_CHOICES, default='Metric')
    notifications_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create or ensure UserProfile exists whenever User is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
