# food_pantry/fixtures/clean_db.py

# This script is used to clean the database by deleting all records from specified tables.
# It is useful for resetting the database to a clean state before populating it with new data.
# It disables foreign key checks to avoid constraint errors during deletion,
# deletes all records from the specified tables, and then re-enables foreign key checks.
# The order of deletion is important to avoid foreign key constraint violations.
# It also logs the actions taken during the cleaning process to a log file.

import sqlite3
from datetime import datetime
from django.core.management import BaseCommand
from common.logger import Logger




# abstract class for logging
class Command(BaseCommand):
    help = "Clean the database by deleting all records from specified tables."

      
    
    def handle(self, *args, **options):
            
            logger = Logger("clean_db") # Initialize the logger

            try:
                logger.info(f" Inicio de limpieza: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                logger.info(" Iniciando limpieza de la base de datos...")
                print(f"🧹 Iniciando limpieza de la base de datos... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                conn = sqlite3.connect("db.sqlite3")
                cursor = conn.cursor()

                # Disable foreign key checks to avoid constraint errors during deletion
                cursor.execute("PRAGMA foreign_keys = OFF;")

                tables = {
                    "volunteer_deliveries_api_volunteerdelivery": "VolunteerDelivery",
                    "delivery_products_api_deliveryproduct": "DeliveryProduct",
                    "deliveries_api_delivery": "Delivery",
                    "products_api_product": "Product",
                    "volunteers_api_volunteer": "Volunteer",
                    "beneficiaries_api_beneficiary": "Beneficiary",
                    "categories_api_category": "Category",
                    "donors_api_donor": "Donor"
                }

                # Delete all records from each table
                for table_name, alias in tables.items():
                    cursor.execute(f"DELETE FROM {table_name};")
                    logger.info(f"  Tabla {alias} ({table_name}) vaciada.")
                    print(f"  Tabla {alias} ({table_name}) vaciada.")


                # Restart autoincremental IDs (SQLite only)
                cursor.execute("DELETE FROM sqlite_sequence;")

                # Re-enable foreign key checks
                cursor.execute("PRAGMA foreign_keys = ON;")

                conn.commit()
                conn.close()

                logger.info(f" Limpieza completada con éxito. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                print(f"✅ Limpieza completada con éxito. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                
            except Exception as e:
                logger.error(f" Error durante la limpieza: {e} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"❌ Error durante la limpieza: {e} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")




'''
# abstract class for logging
class Command(BaseCommand,Logger):
    help = "Clean the database by deleting all records from specified tables."

    def __init__(self):
        super().__init__()
    
    # Initialize the logger
    def handle(self, *args, **options):
            try:
                self.info(f"📆 Inicio de limpieza: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                self.info("🧹 Iniciando limpieza de la base de datos...")

                conn = sqlite3.connect("db.sqlite3")
                cursor = conn.cursor()

                # Disable foreign key checks to avoid constraint errors during deletion
                cursor.execute("PRAGMA foreign_keys = OFF;")

                tables = {
                    "volunteer_deliveries_api_volunteerdelivery": "VolunteerDelivery",
                    "delivery_products_api_deliveryproduct": "DeliveryProduct",
                    "deliveries_api_delivery": "Delivery",
                    "products_api_product": "Product",
                    "volunteers_api_volunteer": "Volunteer",
                    "beneficiaries_api_beneficiary": "Beneficiary",
                    "categories_api_category": "Category",
                    "donors_api_donor": "Donor"
                }

                # Delete all records from each table
                for table_name, alias in tables.items():
                    cursor.execute(f"DELETE FROM {table_name};")
                    self.info(f"  → Tabla {alias} ({table_name}) vaciada.")

                # Restart autoincremental IDs (SQLite only)
                cursor.execute("DELETE FROM sqlite_sequence;")

                # Re-enable foreign key checks
                cursor.execute("PRAGMA foreign_keys = ON;")

                conn.commit()
                conn.close()

                self.info("✅ Limpieza completada con éxito. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                
            except Exception as e:
                self.error(f"❌ Error durante la limpieza: {e} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

'''


