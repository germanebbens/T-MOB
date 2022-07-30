from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Redirect
from django.core.cache import cache
 
@receiver(post_save, sender=Redirect)
def catched_data(sender, instance, **kwargs):
    active_keys = Redirect.objects.filter(active=1)
    for redirect in active_keys.values():
        cache.set(redirect['key'], {'key':redirect['key'], 'url':redirect['url']})
  
