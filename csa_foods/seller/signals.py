# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Restaurant
# from django.contrib.auth.models import Group
#
#
# # Below is to create a restraunt object when someone register as a seller.
# # But it has already dealt in the registration view so we don't need to create it again. It is usefull when someone
# # create a seller object without passing through registration view function(like creating through admin.).
# @receiver(post_save, sender=User)
# def create_restaurant(sender, instance, created, **kwargs):
#     if created and instance.groups.filter(name='sellers').exists():
#         Restaurant.objects.create(seller=instance)
