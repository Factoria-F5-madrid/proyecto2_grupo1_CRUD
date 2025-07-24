from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Cleans and repopulates the database using clean_db and faker_populate_db scripts in fixtures/management/commands folder."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚠️  Starting database rebuild process..."))

        # Step 1: Clean the database
        self.stdout.write(self.style.NOTICE("🧹 Running clean_db..."))
        call_command('clean_db')

        # Step 2: Populate the database with fake data
        self.stdout.write(self.style.NOTICE("🍔 Running faker_populate_db..."))
        call_command('faker_populate_db')

        self.stdout.write(self.style.SUCCESS("✅ Database rebuild completed successfully."))
