from django.core.management.base import BaseCommand

from analytics.tasks import reach


class Command(BaseCommand):
    args = ''
    help = 'Runs worker task to calculate reach and set in cache'

    def handle(self, *args, **options):
        reach.apply_async()
