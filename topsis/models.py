from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    columns = models.IntegerField(default=5)
    weights = models.CharField(max_length=100, default='1,1,1,1,1')
    impacts = models.CharField(max_length=100, default='+,+,+,+,+')
    file = models.TextField(default=None, null=True)
    html = models.TextField(default=None, null=True)
    add = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
