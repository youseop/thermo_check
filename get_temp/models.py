from django.db import models


class Thermal(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    time = models.CharField(default = '', max_length=200)
    student_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def summary(self):
        return self.title + ' / ' + self.pub_date + ' / ' + self.student_name


class User(models.Model):
    text = models.TextField()
