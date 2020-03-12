from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    data = models.CharField(max_length = 60)
    posted = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title
