from django.db import models
from django.utils.translation import ugettext_lazy as _


class Transport(models.Model):
    name = models.CharField(verbose_name = _('Name'), max_length=200)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    type = models.CharField(verbose_name = _('Type Vehicle'), max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = _('Transport Name')
        verbose_name_plural = _('Transport Names')


class Zupynka(models.Model):
    name = models.CharField(verbose_name = _('Name'), max_length=200)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    place = models.FloatField(verbose_name=_('Place by serial number'))
    #type = models.CharField(verbose_name = _('Type Vehicle'), max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = _('Zupynka Name')
        verbose_name_plural = _('Zupynka Names')


class Village(models.Model):
    name = models.CharField(verbose_name = _('Name'), max_length=200)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    zupynks = models.ManyToManyField(Zupynka, verbose_name=_('Zupynka Names'))
    #type = models.CharField(verbose_name = _('Type Vehicle'), max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = _('Village Name')
        verbose_name_plural = _('Village Names')


class RouteBus(models.Model):
    name = models.CharField(verbose_name = _('Name'), max_length=200)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    from_village = models.ForeignKey(Village, verbose_name=_('From village'), related_name='from_village')
    to_village = models.ForeignKey(Village, verbose_name=_('From village'), related_name='to_village')
    across_village = models.ManyToManyField(Village, verbose_name=_('From village'),related_name='across_village')
    #type = models.CharField(verbose_name = _('Type Vehicle'), max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = _('Route Bus Name')
        verbose_name_plural = _('Route Bus Names')

