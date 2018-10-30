from django.test import TestCase
from testapp.models import Band, Member


class BaseTestCase(TestCase):
    
    def setUp(self):
        self.address_one = 'India'
        self.name_one = 'Mahaveer'

        self.address_two = 'Japan'
        self.name_two = 'Rajveer'

        self.member_name = 'Robbert'
        self.member_contact = 9589555555

        self.band_one = Band.objects.create(name=self.name_one, address=self.address_one)
        self.band_two = Band.objects.create(name=self.name_two, address=self.address_two)

        self.member = Member.objects.create(name=self.member_name ,contact=self.member_contact, band=self.band_one)

