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