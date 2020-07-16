from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Picture')
    home = models.CharField(max_length = 40, blank=True)
    school = models.CharField(max_length = 40, blank=True)
    work = models.CharField(max_length = 40, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def edit_home(self, new_home):
        self.home = new_home
        self.save()

    def edit_school(self, new_school):
        self.school = new_school
        self.save()

    def edit_work(self, new_work):
        self.work = new_work
        self.save()

class Location(models.Model):
    name = models.CharField(max_length = 40)
    lat = models.IntegerField()
    lng = models.IntegerField()

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Riot(models.Model):
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return self.description

    def save_riot(self):
        self.save()

    def delete_riot(self):
        self.delete()

    @classmethod
    def get_location_riots(cls,location):
        return cls.objects.filter(location = location)

    class Meta:
        ordering = ['-post_date']