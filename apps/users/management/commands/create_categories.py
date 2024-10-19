from django.core.management.base import BaseCommand

from apps.users.models import Category


class Command(BaseCommand):
    help = 'Create default categories'

    def handle(self, *args, **kwargs):
        categories = [
            {"title": "Mebel", "icon": "bi bi-sofa"},
            {"title": "Chiroq", "icon": "bi bi-lamp"},
            {"title": "Chashka", "icon": "bi bi-cup"},
            {"title": "Stul", "icon": "bi bi-chair"},
            {"title": "Stol", "icon": "bi bi-table"},
            {"title": "Oshxona", "icon": "bi bi-egg"},
            {"title": "Vaza", "icon": "bi bi-bucket"},
            {"title": "Qulf", "icon": "bi bi-lock"},
        ]

        for category_data in categories:
            Category.objects.create(**category_data)
            self.stdout.write(self.style.SUCCESS(
                f"Created category: {category_data['title']}"))
