from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Doner_Post(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 100)
    food_des = models.TextField()
    date_posted = models.DateTimeField (default = timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()

    def __str__(self):
        return self.title

class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to = 'profile_pics')
    number = models.CharField(max_length = 100)
    address= models.CharField(max_length = 100)

    def __str__(self):
        return  f'{self.user.username} Profile'

    def save(self):
        super.save()

        img = Image.open(self.image.path)




