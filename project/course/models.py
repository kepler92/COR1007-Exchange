from django.db import models

# Create your models here.
class course(models.Model):
    time = models.IntegerField('회차', primary_key=True)
    course_start_date = models.DateField('시작일')
    course_end_date = models.DateField('종료일')
    course_place = models.CharField('장소', max_length=100)

    def __str__(self):
        return "{}회차 ({} ~ {})".format(self.time, self.course_start_date, self.course_end_date)