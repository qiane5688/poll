from django.db import models

# Create your models here.
class poll(models.Model):
    title = models.CharField("投票主題", max_length=250)
    date_created = models.DateField("建立日期", auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    title = models.CharField("選項標題", max_length=50)
    count = models.IntegerField("票數")
    poll_id = models.IntegerField("投票主題")

    def __str__(self):
        return str(self.poll_id) + ": " + self.title
 
