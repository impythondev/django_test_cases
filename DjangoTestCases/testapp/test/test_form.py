from .test_base import BaseTestCase
from testapp.forms import BandModelForm


class MemberModelFormTestCase(BaseTestCase):

    # Valid Form Data
    def test_member_model_form_valid(self):
        valid_data = {'name': self.name_one, 'address': self.address_one}

        form = BandModelForm(valid_data)
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_member_model_form_invalid(self):
        invalid_data = {'name': '', 'address': self.address_one}

        form = BandModelForm(invalid_data)
        self.assertFalse(form.is_valid())