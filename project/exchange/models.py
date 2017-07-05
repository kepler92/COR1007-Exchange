from django.db import models
from django.contrib.auth.models import User
from course.models import course

# Create your models here.
class exchange(models.Model):
    user = models.ForeignKey(User)
    haveTime = models.ForeignKey(course, related_name='haveTime')
    wishTimeCheck = models.BooleanField("원하는 시간이 있습니까?", default=True)
    wishTime1 = models.ForeignKey(course, related_name='wishTime1', blank=True, null=True, default=None)
    wishTime2 = models.ForeignKey(course, related_name='wishTime2', blank=True, null=True, default=None)

    def __str__(self):
        return "{} from {}".format(self.id, self.user)