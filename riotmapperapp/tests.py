from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Location,Riot

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

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi', lat= 1.2921, lng= 36.8219)
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

class RiotTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi', lat= 1.2921, lng= 36.8219)
        self.riot = Riot(description = "Teenagers heckling and destroying property", location= self.nairobi)
        self.nairobi.save_location()
        self.riot.save_riot()

    def test_instance(self):
        self.assertTrue(isinstance(self.riot, Riot))

    def tearDown(self):
        Location.objects.all().delete()
        Riot.objects.all().delete()
    
    def test_get_location_riots(self):
        riots = Riot.get_location_riots(self.nairobi)
        self.assertEqual(riots[0].description, 'Teenagers heckling and destroying property')
        self.assertTrue(len(riots) > 0)
    


