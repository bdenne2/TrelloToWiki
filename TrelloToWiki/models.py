from django.db import models

class Token(models.Model):
    name = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
