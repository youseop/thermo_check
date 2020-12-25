from django.db import models


class Thermal(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    student_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def summary(self):
        return self.title + ' / ' + self.pub_date + ' / ' + self.student_name