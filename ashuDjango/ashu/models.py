from django.db import models
from django.utils import timezone
#  able to create model& account
from django.contrib.auth.models import User
# Create your models here.
class ashuvarity(models.Model):
    ASHU_TYPE_CHOICE = [
        ('MA', 'MATH'),
        ('HI', 'HINDI'),
        ('EN', 'ENGLISH'),
        ('CH', 'CHEMISTRY'),
        ('PY', 'PHYSICS'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ashus/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=ASHU_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):                                       
        return self.name
    


# one to many

class AshuReview(models.Model):
    ashu = models.ForeignKey(ashuvarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.ashu.name}'

# Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ashu_varieties = models.ManyToManyField(ashuvarity, related_name='stores')

    def __str__(self):
        return self.name

# One to One 

class AshuCertificate(models.Model):
    ashu = models.OneToOneField(ashuvarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issu_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.ashu.name}'




