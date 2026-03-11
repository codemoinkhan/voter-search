import csv
import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from voters.models import Voter, Location

# CSV_PATH = "../../data/voters.csv"
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "voters.csv")

with open(CSV_PATH, newline="",  encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        location, _ = Location.objects.get_or_create(
            district=row["district"],
            block=row["block"],
            gram_panchayat=row["gram_panchayat"],
            ward=row["ward"],
            polling_station=row["polling_station"],
            polling_booth=row["booth"],
            village=row["village"],
        )

        Voter.objects.create(
            serial_number=row["serial"],
            house_number=row["house_no"],
            name_hindi=row["name"],
            father_name=row["father_name"],
            voter_id=row["voter_id"],
            gender=row["gender"],
            age=row["age"],
            location=location
        )

print("CSV import completed")