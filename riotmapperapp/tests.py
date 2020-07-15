from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTestClass(TestCase):
    def setUp(self):
        self.lorna = User(username="lorna", email="lorna@gmail.com", password="1234")
        self.profile = Profile(user= self.lorna, profile_pic='mepng', home='Nairobi, Kenya', school='Moringa', work='Stackoverflow')
        self.lorna.save()
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lorna, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_edit_home(self):
        self.profile.edit_home('Limuru, Kenya')
        self.assertEqual(self.profile.home, 'Limuru, Kenya')

    def test_edit_work(self):
        self.profile.edit_work('Google')
        self.assertEqual(self.profile.work, 'Google')

    def test_edit_school(self):
        self.profile.edit_school('Havard')
        self.assertEqual(self.profile.school, 'Havard')


