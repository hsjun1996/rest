from django.db import models
import datetime
# Create your models here.
class Reservation(models.Model) :
    userid = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True,default=datetime.date.today)
    people = models.IntegerField()
    isCheck = models.BooleanField(default=False)

    def __str__(self):
        return self.userid
