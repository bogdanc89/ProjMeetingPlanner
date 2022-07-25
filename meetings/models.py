from email.policy import default
from datetime import time

from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    floornumber = models.IntegerField(default=0)
    roomnumber = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f" Room:{self.name} / Room Number :{self.roomnumber} at {self.floornumber} floor"


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration =models.IntegerField(default=1)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.title} at {self.start_time} on {self.date}"

