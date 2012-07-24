from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

from campaigns.managers import CampaignManager


class Variant(models.Model):
    """
    Model representing a presentational variant of the IDL message being
    broadcast. Implementors are able to choose which of these to use.
    """
    name = models.CharField(_('Name'), max_length=16)
    slug = models.SlugField(_('Slug'), max_length=16)

    class Meta:
        verbose_name = 'Presentation Variant'
        verbose_name_plural = 'Presentation Variant'

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    """
    Model representing an IDL campaign.
    """
    name = models.CharField(_('Name'), max_length=128)
    slug = models.SlugField(_('Slug'), max_length=32)
    is_active = models.BooleanField(_('Is Active?'), default=False)
    message = models.TextField(_('Message'),
        blank=True
    )

    objects = CampaignManager()

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'

    def __unicode__(self):
        return self.name

    def template(self, variant):
        """
        Returns the name of the template a campaign should use for the passed
        variant.
        """
        return 'campaigns/%s.html' % variant


def invalidate_cache(sender, instance, created, **kwargs):
    """
    Clear cache of all IncludeView responses whenever a change is made to a
    Campaign object.
    """
    if not created:
        cache.clear()
post_save.connect(invalidate_cache, sender=Campaign)
