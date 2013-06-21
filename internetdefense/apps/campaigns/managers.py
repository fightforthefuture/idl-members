from django.db import models


class CampaignManager(models.Manager):
    """
    Custom manager for the Campaign model. Provides additional methods for
    working with active campaigns.
    """

    def latest(self):
        qs = self.active().order_by('-id')
        try:
            return qs[0]
        except IndexError:
            return self.none()

    def active(self):
        return self.get_query_set().filter(is_active=True)
