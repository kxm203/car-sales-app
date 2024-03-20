#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

fake = Faker()

class FordMustang:
    def __init__(self, image):
        self.model = "Mustang"
        self.year = fake.random_int(min=1965, max=2004)
        self.color = fake.color_name()
        self.price = fake.random_float(min=4999.99, max=125000.99)
        self.image = image

    def __repr__(self):
        return f"<FordMustang {self.year} {self.color} - Image: {self.image}>"

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Generate 10 instances of FordMustang with random image URLs
        mustangs = [FordMustag(fake.image_url()) for _ in range(10)]
