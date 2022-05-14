from django.db import models
from user.models import User

from helpers.db_helper import BaseAbstractModel



class Employee(BaseAbstractModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    avatar = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
