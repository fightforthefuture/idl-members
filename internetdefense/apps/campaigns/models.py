from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save

from campaigns.managers import CampaignManager


class Variant(models.Model):
    """
    Model representing a presentational variant of the IDL message being
    broadcast. Implementors are able to choose which of these to use.
    """
    name = models.CharField('Name', max_length=16)
    slug = models.SlugField('Slug', max_length=16)

    class Meta:
        verbose_name = 'Presentation Variant'
        verbose_name_plural = 'Presentation Variant'

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    """
    Model representing an IDL campaign.
    """
    name = models.CharField('Name', max_length=128)
    slug = models.SlugField('Slug', max_length=32)
    is_active = models.BooleanField('Is Active?', default=False)
    message = models.TextField('Message',
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
        return 'campaigns/%s/%s.html' % (self.slug, variant,)


def invalidate_cache(sender, instance, created, **kwargs):
    """
    Clear cache of all IncludeView responses whenever a change is made to a
    Campaign object.
    """
    if not created:
        cache.clear()
post_save.connect(invalidate_cache, sender=Campaign)


def clear_cloudflare_cache(sender, instance, created, **kwargs):
        import os, re, urllib, urllib2
        cloudflare_url = 'https://www.cloudflare.com/api_json.html'
        domain = 'internetdefenseleague.org'
        data = {
            'a': 'fpurge_ts',
            'tkn': os.environ.get('CLOUDFLARE_API_KEY'),
            'email': 'team@fightforthefuture.org',
            'z': domain,
            'v': '1'
        }
        encoded_data = urllib.urlencode(data)
        result = urllib2.urlopen(cloudflare_url, encoded_data)
        print result.read()
post_save.connect(clear_cloudflare_cache, sender=Campaign)
