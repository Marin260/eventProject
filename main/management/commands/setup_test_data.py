from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import (
    MjestoFactory,
    EventFactory
)

NUM_MJESTOS = 10
NUM_EVENTS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Mjesto, Event]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_MJESTOS):
            author = MjestoFactory()
        
        for _ in range(NUM_EVENTS):
            author = EventFactory()
