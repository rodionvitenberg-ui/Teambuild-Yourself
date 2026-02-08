import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)

    class Meta:
        db_table = 'users_user'

class SubscriptionTier(models.TextChoices):
    FREE = 'FREE', _('Free')
    PRO = 'PRO', _('Pro')
    TEAM = 'TEAM', _('Team')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    timezone = models.CharField(max_length=50, default='UTC')  # [cite: 9]
    subscription_tier = models.CharField(
        max_length=10, 
        choices=SubscriptionTier.choices, 
        default=SubscriptionTier.FREE
    )
    avatar_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, max_length=500)
    global_streak = models.IntegerField(default=0)
    metadata = models.JSONField(default=dict, blank=True)  # [cite: 23]

    def __str__(self):
        return f"{self.user.username} ({self.subscription_tier})"