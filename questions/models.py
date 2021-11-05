from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey('questions.models.Profile', on_delete=models.CASCADE, related_name='questions')
    published_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tags',related_name='questions')
    text = models.TextField()
    STATUS_CHOICES = [
        ('t', 'Closet'),
        ('a', 'Available')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')

class Profile(models.Model):
    nickname = models.CharField(max_length=256)
    link = models.URLField(max_length=256,blank=True, null=True)
    def __str__(self):
        return ' '.join([self.nickname])

class Tag(models.Model):
    name = models.CharField(max_length=256)
