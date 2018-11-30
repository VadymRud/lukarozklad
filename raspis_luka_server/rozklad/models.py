from django.db import models
from django.utils.translation import ugettext_lazy as _

class Transport(models.Model):
    name = models.CharField(verbose_name = _('Name'),max_length=200)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Transport Name')
        verbose_name_plural = _('Transport Names')

