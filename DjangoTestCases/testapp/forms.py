from django import forms
from .models import Band


class BandModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BandModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Band
        fields = '__all__'
