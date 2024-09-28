import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.categories.models import Category
from apps.products.models import Product


class Command(BaseCommand):
    help = "Generate fake data for Products and Categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate Categories
        self.stdout.write("Generating categories...")
        for _ in range(10):
            category = Category.objects.create(
                name=fake.word(),
                description=fake.text(max_nb_chars=100)
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created category: {category.name}"))

        # Get all categories for assigning to products
        categories = Category.objects.all()

        # Generate Products
        self.stdout.write("Generating products...")
        for _ in range(50):
            product = Product.objects.create(
                name=fake.name(),
                category=random.choice(categories),
                description=fake.text(max_nb_chars=200)
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created product: {product.name}"))

        self.stdout.write(self.style.SUCCESS(
            "Successfully generated fake data!"))
