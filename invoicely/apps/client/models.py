from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    org_number = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_reference = models.CharField(max_length=255, blank=True, null=True)
    # related_name is used to get all clients from users, on_delete param specifies, if user is deleted, all 
    # clients are deleted as well.
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    #  This is toString in Python
    def __str__(self):
        return '%s' % self.name