from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:30]