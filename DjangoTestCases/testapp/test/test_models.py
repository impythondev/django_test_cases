from django.test import TestCase

from .test_base import BaseTestCase
from testapp.models import Band, Member


class BandTestCase(BaseTestCase):

    def test_band_address(self):
        band = Band.objects.get(name=self.name_one)
        self.assertEqual(band.get_name_with_address(), 'Mahaveer from India')


class MemberTestCase(BaseTestCase):

    def test_member_band(self):
        member = Member.objects.get(band=self.band_one)
        self.assertEqual(member.band.name, self.name_one)