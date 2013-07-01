from django.db import models
from django.utils.translation import ugettext as _

from campaigns.models import Campaign, Variant


class Impression(models.Model):
    """
    Model for a single impression of an IDL message
    """
    time = models.DateTimeField(_('Date'),
        auto_now_add=True
    )
    ip = models.IPAddressField(_('IP Address'),
        blank=True,
        null=True
    )
    campaign = models.ForeignKey(Campaign,
        blank=True,
        null=True
    )
    embedding_url = models.URLField(_('Embedding URL'),
        blank=True,
        null=True,
        max_length=1024
    )
    embedding_host = models.CharField(_('Embedding Hostname'),
        blank=True,
        null=True,
        max_length=256
    )
    custom_url = models.URLField(_('Custom URL used'),
        blank=True,
        null=True,
        max_length=1024
    )
    variant = models.ForeignKey(Variant,
        blank=True,
        null=True
    )
    is_autobroadcast = models.BooleanField(_('Autobroadcasted?'),
        default=False
    )

    def __unicode__(self):
        return '%s at %s' % (self.ip, self.time,)
