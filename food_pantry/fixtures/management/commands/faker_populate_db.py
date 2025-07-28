# food_pantry/fixtures/faker_populate_db.py
# Script to populate the database with fake data using Faker
# This script uses the Faker library to generate realistic fake data for the food pantry database.
# It populates tables such as Donor, Category, Product, Beneficiary, Delivery,
# DeliveryProduct, Volunteer, and VolunteerDelivery with random data.


import sqlite3
from faker import Faker
from random import randint, choice
from datetime import date, datetime

from django.core.management import BaseCommand
from common.logger import Logger


class Command(BaseCommand):
    help = "Populate the database with fake data for testing purposes."

    def handle(self, *args, **options):

        logger = Logger("populate_db")  # Initialize the logger

        fake = Faker('es_ES')  # Use Spanish locale for Faker
        Num_records = 15  # Number of records to insert in each table

        try:
            logger.info(f" Inicio de carga: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info(f" Iniciando poblamiento de la base de datos con Faker...\n")
            print(f"🚀 Iniciando poblamiento de la base de datos con Faker... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()

            

            # --- DONOR ---
            donor_ids = []
            logger.info(" Introduciendo donantes (Donor)...")
            print("👤 Introduciendo donantes (Donor)...")
            for i in range(Num_records):
                name = fake.name()
                tipo = choice(["individual", "institución"])
                contact = fake.phone_number()
                anonymous = randint(0, 1)
                cursor.execute(
                    "INSERT INTO donors_api_donor (name, type, contact, anonymous) VALUES (?, ?, ?, ?)",
                    (name, tipo, contact, anonymous)
                )
                donor_ids.append(cursor.lastrowid)
                logger.info(f"   Donante {i+1}: {name}, tipo: {tipo}, contacto: {contact}, anónimo: {anonymous}")
                print(f"  → Donante {i+1}: {name}, tipo: {tipo}, contacto: {contact}, anónimo: {anonymous}")
            logger.info(f"   {len(donor_ids)} donantes añadidos.\n")
            print(f"  → {len(donor_ids)} donantes añadidos.\n")


            # --- CATEGORY ---
            category_ids = []
            logger.info("\n Introduciendo categorías (Category)...")
            print("📦 Introduciendo categorías (Category)...")
            for i in range(Num_records):
                name = fake.word().capitalize()
                description = fake.text(max_nb_chars=40)
                cursor.execute(
                    "INSERT INTO categories_api_category (name, description) VALUES (?, ?)",
                    (name, description)
                )
                category_ids.append(cursor.lastrowid)
                logger.info(f"   Categoría {i+1}: {name} - {description}")
                print(f"  → Categoría {i+1}: {name} - {description}")
            logger.info(f"   {len(category_ids)} categorías creadas.\n")
            print(f"  → {len(category_ids)} categorías creadas.\n")

            # --- PRODUCT ---
            product_ids = []
            logger.info("\n Introduciendo productos (Product)...")
            print("🛒 Introduciendo productos (Product)...")
            for i in range(Num_records):
                name = fake.word().capitalize()
                quantity = randint(5, 50)
                expiration_date = fake.future_date().isoformat()
                category_id = choice(category_ids)
                donor_id = choice(donor_ids)
                cursor.execute(
                    "INSERT INTO products_api_product (name, quantity, expiration_date, category_id, donor_id) VALUES (?, ?, ?, ?, ?)",
                    (name, quantity, expiration_date, category_id, donor_id)
                )
                product_ids.append(cursor.lastrowid)
                logger.info(f"   Producto {i+1}: {name}, cantidad: {quantity}, expira: {expiration_date}, donor_id: {donor_id}, category_id: {category_id}")
                print(f"  → Producto {i+1}: {name}, cantidad: {quantity}, expira: {expiration_date}, donor_id: {donor_id}, category_id: {category_id}")
            logger.info(f"   {len(product_ids)} productos añadidos.\n")
            print(f"  → {len(product_ids)} productos añadidos.\n")


            # --- BENEFICIARY ---
            beneficiary_ids = []
            logger.info(" Introduciendo beneficiarios (Beneficiary)...")
            print("🏠 Introduciendo beneficiarios (Beneficiary)...")
            for i in range(Num_records):
                    name = fake.name()
                    address = fake.street_address()
                    contact_info = fake.phone_number()
                    cursor.execute(
                        "INSERT INTO beneficiaries_api_beneficiary (name, address, contact_info) VALUES (?, ?, ?)",
                        (name, address, contact_info)
                    )
                    beneficiary_ids.append(cursor.lastrowid)
                    logger.info(f"   Beneficiario {i+1}: {name}, dirección: {address}, contacto: {contact_info}")
                    print(f"  → Beneficiario {i+1}: {name}, dirección: {address}, contacto: {contact_info}")
            logger.info(f"   {len(beneficiary_ids)} beneficiarios añadidos.\n")
            print(f"  → {len(beneficiary_ids)} beneficiarios añadidos.\n")

            # --- DELIVERY ---
            delivery_ids = []
            logger.info(" Insertando entregas (Delivery)...")
            print("🚚 Insertando entregas (Delivery)...")
            for i, beneficiary_id in enumerate(beneficiary_ids):
                    delivery_date = date.today().isoformat()
                    address = fake.street_address()
                    cursor.execute(
                        "INSERT INTO deliveries_api_delivery (delivery_date, beneficiary_id, address) VALUES (?, ?, ?)",
                        (delivery_date, beneficiary_id, address)
                    )
                    delivery_ids.append(cursor.lastrowid)
                    logger.info(f"   Entrega {i+1}: fecha: {delivery_date}, dirección: {address}")
                    print(f"  → Entrega {i+1}: fecha: {delivery_date}, dirección: {address}, beneficiary_id: {beneficiary_id}")
            logger.info(f"   {len(delivery_ids)} entregas registradas.\n")
            print(f"  → {len(delivery_ids)} entregas registradas.\n")   
            

            # --- DELIVERYPRODUCT ---
            logger.info(" Asignando productos a entregas (DeliveryProduct)...")
            print("📦 Asignando productos a entregas (DeliveryProduct)...")
            for i, delivery_id in enumerate(delivery_ids):
                    product_id = choice(product_ids)
                    quantity = randint(1, 10)
                    cursor.execute(
                        "INSERT INTO delivery_products_api_deliveryproduct (quantity_delivered, delivery_id, product_id) VALUES (?, ?, ?)",
                        (quantity, delivery_id, product_id)
                    )
                    logger.info(f"   Producto {product_id} asignado a entrega {delivery_id} (cantidad: {quantity})")
                    print(f"  → Producto {product_id} asignado a entrega {delivery_id} (cantidad: {quantity})")
            logger.info(f"   Productos asignados a entregas.\n")
            print(f"  → Productos asignados a entregas.\n")

            # --- VOLUNTEER ---
            volunteer_ids = []
            logger.info(" Añadiendo voluntarios (Volunteer)...")
            print("🙋 Añadiendo voluntarios (Volunteer)...")
            for i in range(Num_records):
                    name = fake.name()
                    email = fake.email()
                    cursor.execute(
                        "INSERT INTO volunteers_api_volunteer (name, email) VALUES (?, ?)",
                        (name, email)
                    )
                    volunteer_ids.append(cursor.lastrowid)
                    logger.info(f"   Voluntario {i+1}: {name}, email: {email}")
                    print(f"  → Voluntario {i+1}: {name}, email: {email}")
            logger.info(f"   {len(volunteer_ids)} voluntarios registrados.\n")
            print(f"  → {len(volunteer_ids)} voluntarios registrados.\n")
            

            # --- VOLUNTEERDELIVERY ---
            logger.info(" Asignando voluntarios a entregas (VolunteerDelivery)...")
            print("👥 Asignando voluntarios a entregas (VolunteerDelivery)...")
            for i, delivery_id in enumerate(delivery_ids):
                    volunteer_id = choice(volunteer_ids)
                    cursor.execute(
                        "INSERT INTO volunteer_deliveries_api_volunteerdelivery (volunteer_id, delivery_id) VALUES (?, ?)",
                        (volunteer_id, delivery_id)
                    )
                    logger.info(f"   Voluntario {volunteer_id} asignado a entrega {delivery_id}")
                    print(f"  → Voluntario {volunteer_id} asignado a entrega {delivery_id}")
            logger.info(f"   Voluntarios asignados a entregas.\n")
            print(f"  → Voluntarios asignados a entregas.\n")

            conn.commit()
            conn.close()
            logger.info(f" Carga de datos completada con éxito. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"✅ Carga de datos completada con éxito. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
        except Exception as e:
            logger.error(f" Error durante la carga de datos: {e} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"❌ Error durante la carga de datos: {e} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")














'''
fake = Faker()
LOG_PATH = "fixtures/faker-populate-db-log.txt"

def log(message):
    print(message)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(message + "\n")

try:
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    log("🚀 Iniciando poblamiento/carga de datos en la base de datos con Faker....\n")

    tables = {
        "donors_api_donor": "Donor",
        "categories_api_category": "Category",
        "products_api_product": "Product",
        "beneficiaries_api_beneficiary": "Beneficiary",
        "deliveries_api_delivery": "Delivery",
        "delivery_products_api_deliveryproduct": "DeliveryProduct",
        "volunteers_api_volunteer": "Volunteer",
        "volunteer_deliveries_api_volunteerdelivery": "VolunteerDelivery"
    }

    Num_records = 15 # Number of records to insert in each table

    # Donor
    donor_ids = []
    log("👤 Introduciendo donantes (Donor)...")
    for i in range(Num_records):
        name = fake.name()
        tipo = choice(["individual", "institución"])
        contact = fake.phone_number()
        anonymous = randint(0, 1)
        cursor.execute(
            "INSERT INTO donors_api_donor (name, type, contact, anonymous) VALUES (?, ?, ?, ?)",
            (name, tipo, contact, anonymous)
        )
        donor_ids.append(cursor.lastrowid)
        log(f"  → Donante {i+1}: {name}, tipo: {tipo}, contacto: {contact}, anónimo: {anonymous}")
    log(f"  → {len(donor_ids)} donantes añadidos.\n")




    # Category
    category_ids = []
    log("\n📦 Introduciendo categorías (Category)...")
    for i in range(Num_records):
        name = fake.word().capitalize()
        description = fake.text(max_nb_chars=40)
        cursor.execute(
            "INSERT INTO categories_api_category (name, description) VALUES (?, ?)",
            (name, description)
        )
        category_ids.append(cursor.lastrowid)
        log(f"  → Categoría {i+1}: {name} - {description}")
    log(f"  → {len(category_ids)} categorías creadas.\n")



    # Product
    product_ids = []
    log("\n🛒 Introduciendo productos (Product)...")
    for i in range(Num_records):
        name = fake.word().capitalize()
        quantity = randint(5, 50)
        expiration_date = fake.future_date().isoformat()
        category_id = choice(category_ids)
        donor_id = choice(donor_ids)
        cursor.execute(
            "INSERT INTO products_api_product (name, quantity, expiration_date, category_id, donor_id) VALUES (?, ?, ?, ?, ?)",
            (name, quantity, expiration_date, category_id, donor_id)
        )
        product_ids.append(cursor.lastrowid)
        log(f"  → Producto {i+1}: {name}, cantidad: {quantity}, expira: {expiration_date}, donor_id: {donor_id}, category_id: {category_id}")
    log(f"  → {len(product_ids)} productos añadidos.\n")



    # Beneficiary
    beneficiary_ids = []
    log("\n🏠 Introduciendo beneficiarios (Beneficiary)...")
    for i in range(Num_records):
        name = fake.name()
        address = fake.street_address()
        contact_info = fake.phone_number()
        cursor.execute(
            "INSERT INTO beneficiaries_api_beneficiary (name, address, contact_info) VALUES (?, ?, ?)",
            (name, address, contact_info)
        )
        beneficiary_ids.append(cursor.lastrowid)
        log(f"  → Beneficiario {i+1}: {name}, dirección: {address}, contacto: {contact_info}")
    log(f"  → {len(beneficiary_ids)} beneficiarios añadidos.\n")



    # Delivery
    delivery_ids = []
    log("\n🚚 Insertando entregas (Delivery)...")
    # Randomly select a beneficiary for each delivery
    for i, beneficiary_id in enumerate(beneficiary_ids):
        delivery_date = date.today().isoformat()
        address = fake.street_address()
        cursor.execute(
            "INSERT INTO deliveries_api_delivery (delivery_date, beneficiary_id, address) VALUES (?, ?, ?)",
            (delivery_date, beneficiary_id, address)
        )
        delivery_ids.append(cursor.lastrowid)
        log(f"  → Entrega {i+1}: fecha: {delivery_date}, dirección: {address}, beneficiary_id: {beneficiary_id}")
    log(f"  → {len(delivery_ids)} entregas registradas.\n")


    # DeliveryProduct
    log("\n📦 Asignando productos a entregas (DeliveryProduct)...")
    for i, delivery_id in enumerate(delivery_ids):
        product_id = choice(product_ids)
        quantity = randint(1, 10)
        cursor.execute(
            "INSERT INTO delivery_products_api_deliveryproduct (quantity_delivered, delivery_id, product_id) VALUES (?, ?, ?)",
            (quantity, delivery_id, product_id)
        )
        log(f"  → Producto {product_id} asignado a entrega {delivery_id} con cantidad: {quantity}")
    log(f"  → Productos asignados a entregas.\n")


    # Volunteer
    volunteer_ids = []
    log("\n🙋 Añadiendo voluntarios (Volunteer)...")
    for i in range(Num_records):
        name = fake.name()
        email = fake.email()
        cursor.execute(
            "INSERT INTO volunteers_api_volunteer (name, email) VALUES (?, ?)",
            (name, email)
        )
        volunteer_ids.append(cursor.lastrowid)
        log(f"  → Voluntario {i+1}: {name}, email: {email}")
    log(f"  → {len(volunteer_ids)} voluntarios registrados.\n")



    # VolunteerDelivery
    log("\n👥 Asignando voluntarios a entregas...")
    for i, delivery_id in enumerate(delivery_ids):
        volunteer_id = choice(volunteer_ids)
        cursor.execute(
            "INSERT INTO volunteer_deliveries_api_volunteerdelivery (volunteer_id, delivery_id) VALUES (?, ?)",
            (volunteer_id, delivery_id)
        )
        log(f"  → Voluntario {volunteer_id} asignado a entrega {delivery_id}")
    log(f"  → Voluntarios asignados a entregas.\n")


    conn.commit()
    conn.close()
    log("\n✅ Carga de datos completada con éxito.")

except Exception as e:
    log(f"\n❌ Error durante la carga de datos: {e}")
'''