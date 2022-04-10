from django.db import models


class profilePic(models.Model):
    user = models.CharField(max_length=100)
    pic = models.CharField(max_length=500)
    def __str__(self):
        return self.user


class notificationsmMention(models.Model):
    myuser = models.CharField(max_length=100, blank=True)
    user = models.CharField(max_length=100)
    to_pk = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True)
    def __str__(self) -> str:
        return self.user
    class Meta:
        ordering = ['-id']


class notificationsmLike(models.Model):
    myuser = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    to_pk = models.CharField(max_length=100)
    class Meta:
        ordering = ['-id']



class comment(models.Model):
    to_pk = models.BigIntegerField(blank=True)
    user = models.CharField(max_length=100, blank=True)
    Comment = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self) -> str:
        return self.Comment
    class Meta:
        ordering = ['-id']

class post(models.Model):
    user = models.CharField(max_length=100, blank=True)
    Content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'{self.Content}'

    class Meta:
        ordering = ['-id']

class ver(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user