from django.db import models
from django.utils.translation import gettext as _


class Band(models.Model):
    name = models.CharField(verbose_name=_('Band'), max_length=20)
    address = models.CharField(verbose_name=_('Address'), max_length=256)

    def get_name_with_address(self):
        return '{0} from {1}'.format(self.name, self.address)

    def __str__(self):
        return '{0}'.format(self.name)


class Member(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=20)
    contact = models.IntegerField(verbose_name=_('Name'))

    band = models.ForeignKey(Band, verbose_name=_('Band'), related_name=_('members'))

    def __str__(self):
        return '{0}'.format(self.name)
